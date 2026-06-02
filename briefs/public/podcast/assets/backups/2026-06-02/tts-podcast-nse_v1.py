#!/usr/bin/env python3
"""
TTS podcast generator for the NSE Daily Brief.

Reads today's podcast script (produced by /podcast-script-public-nse),
calls the Sarvam TTS API chunk by chunk, concatenates the audio,
optionally adds intro/outro music with fade in/out, normalizes
loudness, and writes the final MP3 to briefs/public/podcast/{date}/audio.mp3.

Usage:
    python tts-podcast-nse.py                       # today's date
    python tts-podcast-nse.py --date 2026-05-29     # specific date
    python tts-podcast-nse.py --voice pavithra      # override voice
    python tts-podcast-nse.py --no-music            # skip intro/outro
    python tts-podcast-nse.py --no-normalize        # skip loudness fix
    python tts-podcast-nse.py --dry-run             # parse + chunk only, no API calls

Dependencies:
    pip install requests pydub
    brew install ffmpeg   (macOS; pydub uses ffmpeg under the hood)

API key:
    Saved at <CANONICAL_ROOT>/sarvam_api_key.txt (single line, no quotes).
"""

import argparse
import base64
import io
import re
import sys
import time
from datetime import date, datetime, timezone, timedelta

# IST timezone — see market-data-public-nse.py for rationale (travel-proof, brief dating)
IST = timezone(timedelta(hours=5, minutes=30))

def today_ist() -> str:
    """Return today's date in IST as YYYY-MM-DD, regardless of system timezone."""
    return datetime.now(IST).date().isoformat()
from pathlib import Path

import requests
from pydub import AudioSegment


# ---------- Config ----------

CANONICAL_ROOT = Path("/Users/nimitmehra/Manus/NSE-Tracker")
BRIEFS_PODCAST_DIR = CANONICAL_ROOT / "briefs" / "public" / "podcast"
ASSETS_DIR = BRIEFS_PODCAST_DIR / "assets"
BACKUPS_ROOT = CANONICAL_ROOT / "backups"
API_KEY_FILE = CANONICAL_ROOT / "sarvam_api_key.txt"

SARVAM_API_URL = "https://api.sarvam.ai/text-to-speech"
DEFAULT_VOICE = "meera"
DEFAULT_LANGUAGE = "en-IN"
DEFAULT_MODEL = "bulbul:v1"
MAX_CHARS_PER_CHUNK = 500       # Sarvam bulbul:v1 per-input limit
MAX_INPUTS_PER_REQUEST = 3      # Sarvam per-request limit
INTER_CHUNK_PAUSE_MS = 250
INTER_REQUEST_DELAY_S = 0.4     # avoid rate limits
TARGET_DBFS = -16.0             # podcast standard loudness

INTRO_FILENAME = "intro_v1.mp3"
OUTRO_FILENAME = "outro_v1.mp3"


# ---------- Helpers ----------

def fatal(msg: str, code: int = 1) -> None:
    print(f"FATAL: {msg}", file=sys.stderr)
    sys.exit(code)


def load_api_key() -> str:
    if not API_KEY_FILE.exists():
        fatal(
            f"Sarvam API key file missing at {API_KEY_FILE}\n"
            f"Sign up at https://sarvam.ai, grab your API key, save it as a single line in the file above."
        )
    key = API_KEY_FILE.read_text(encoding="utf-8").strip()
    if not key:
        fatal(f"Sarvam API key file is empty: {API_KEY_FILE}")
    return key


def strip_script_metadata(script_text: str) -> str:
    """Drop everything above the first '---' separator (frontmatter / metadata)."""
    if "\n---\n" not in script_text:
        fatal("Script missing '---' separator after metadata header. Re-run /podcast-script-public-nse.")
    return script_text.split("\n---\n", 1)[1].strip()


def strip_say_hints(text: str) -> str:
    """Drop pronunciation hints like '[SAY: KHAH-rif]' — Sarvam doesn't use them."""
    return re.sub(r"\s*\[SAY:\s*[^\]]+\]", "", text)


def chunk_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> list[str]:
    """
    Split text into chunks under max_chars, respecting sentence boundaries.
    If a single sentence exceeds max_chars, fall back to comma boundaries,
    then to a hard split.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks: list[str] = []
    current = ""

    for sent in sentences:
        if len(sent) > max_chars:
            if current:
                chunks.append(current)
                current = ""
            parts = re.split(r"(?<=,)\s+", sent)
            sub = ""
            for p in parts:
                if len(p) > max_chars:
                    if sub:
                        chunks.append(sub)
                        sub = ""
                    for i in range(0, len(p), max_chars):
                        chunks.append(p[i : i + max_chars])
                elif len(sub) + len(p) + 1 <= max_chars:
                    sub = (sub + " " + p).strip()
                else:
                    chunks.append(sub)
                    sub = p
            if sub:
                chunks.append(sub)
        elif len(current) + len(sent) + 1 <= max_chars:
            current = (current + " " + sent).strip()
        else:
            if current:
                chunks.append(current)
            current = sent

    if current:
        chunks.append(current)
    return [c for c in chunks if c.strip()]


def call_sarvam_tts(
    chunks_batch: list[str],
    api_key: str,
    voice: str,
    model: str = DEFAULT_MODEL,
) -> list[bytes]:
    """
    Call Sarvam TTS with up to MAX_INPUTS_PER_REQUEST chunks.
    Returns a list of WAV byte buffers, one per input chunk.
    """
    headers = {
        "Content-Type": "application/json",
        "api-subscription-key": api_key,
    }
    payload = {
        "inputs": chunks_batch,
        "target_language_code": DEFAULT_LANGUAGE,
        "speaker": voice,
        "pitch": 0,
        "pace": 1.0,
        "loudness": 1.0,
        "speech_sample_rate": 22050,
        "enable_preprocessing": True,
        "model": model,
    }
    resp = requests.post(SARVAM_API_URL, headers=headers, json=payload, timeout=120)
    if not resp.ok:
        try:
            err_body = resp.json()
        except Exception:
            err_body = resp.text
        fatal(f"Sarvam API error {resp.status_code}: {err_body}")

    data = resp.json()
    audios_b64 = data.get("audios", [])
    if not audios_b64:
        fatal(f"Sarvam returned no audio. Full response: {data}")
    return [base64.b64decode(a) for a in audios_b64]


def generate_audio(
    script_text: str,
    api_key: str,
    voice: str,
    verbose: bool = False,
) -> AudioSegment:
    chunks = chunk_text(script_text)
    if verbose:
        print(f"[INFO] Script split into {len(chunks)} TTS chunks")

    segments: list[AudioSegment] = []
    for batch_start in range(0, len(chunks), MAX_INPUTS_PER_REQUEST):
        batch = chunks[batch_start : batch_start + MAX_INPUTS_PER_REQUEST]
        if verbose:
            print(f"[INFO] Calling Sarvam for chunks {batch_start + 1}-{batch_start + len(batch)} / {len(chunks)}")
        wav_buffers = call_sarvam_tts(batch, api_key, voice)
        for wav_bytes in wav_buffers:
            seg = AudioSegment.from_wav(io.BytesIO(wav_bytes))
            segments.append(seg)
            segments.append(AudioSegment.silent(duration=INTER_CHUNK_PAUSE_MS))
        time.sleep(INTER_REQUEST_DELAY_S)

    if not segments:
        fatal("No audio segments produced — script may be empty after stripping.")

    combined = segments[0]
    for seg in segments[1:]:
        combined = combined + seg
    return combined


def add_intro_outro(
    speech: AudioSegment,
    intro_path: Path,
    outro_path: Path,
    verbose: bool = False,
) -> AudioSegment:
    final = speech
    if intro_path.exists():
        intro = AudioSegment.from_file(str(intro_path)).fade_in(200).fade_out(800)
        final = intro + AudioSegment.silent(duration=400) + final
        if verbose:
            print(f"[INFO] Intro added from {intro_path.name} ({intro.duration_seconds:.1f}s)")
    elif verbose:
        print(f"[INFO] No intro at {intro_path} — skipping")

    if outro_path.exists():
        outro = AudioSegment.from_file(str(outro_path)).fade_in(800).fade_out(1500)
        final = final + AudioSegment.silent(duration=400) + outro
        if verbose:
            print(f"[INFO] Outro added from {outro_path.name} ({outro.duration_seconds:.1f}s)")
    elif verbose:
        print(f"[INFO] No outro at {outro_path} — skipping")
    return final


def normalize_loudness(audio: AudioSegment, target_dbfs: float = TARGET_DBFS) -> AudioSegment:
    if audio.dBFS == float("-inf"):
        return audio
    return audio.apply_gain(target_dbfs - audio.dBFS)


def backup_existing_output(output_path: Path, target_date: str) -> None:
    if not output_path.exists():
        return
    backup_dir = BACKUPS_ROOT / datetime.now().strftime("%Y-%m-%d")
    backup_dir.mkdir(parents=True, exist_ok=True)
    n = 1
    while (backup_dir / f"audio_{target_date}_v{n}.mp3").exists():
        n += 1
    backup_path = backup_dir / f"audio_{target_date}_v{n}.mp3"
    output_path.rename(backup_path)
    print(f"[INFO] Existing audio backed up to {backup_path}")


# ---------- Main ----------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate NSE Daily Brief podcast MP3 from script")
    parser.add_argument("--date", default=today_ist(), help="Brief date YYYY-MM-DD (defaults to today in IST, NOT system tz)")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help=f"Sarvam voice ID (default: {DEFAULT_VOICE})")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Sarvam model (default: {DEFAULT_MODEL})")
    parser.add_argument("--no-music", action="store_true", help="Skip intro/outro music")
    parser.add_argument("--no-normalize", action="store_true", help="Skip loudness normalization")
    parser.add_argument("--dry-run", action="store_true", help="Parse + chunk only; no API calls, no audio file")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    date_dir = BRIEFS_PODCAST_DIR / args.date
    script_path = date_dir / "script.md"
    if not script_path.exists():
        fatal(
            f"Script not found at {script_path}\n"
            f"Run /podcast-script-public-nse for date {args.date} first."
        )

    script_raw = script_path.read_text(encoding="utf-8")
    script_body = strip_script_metadata(script_raw)
    script_clean = strip_say_hints(script_body)

    chars = len(script_clean)
    words = len(script_clean.split())
    chunks = chunk_text(script_clean)
    print(f"[INFO] Script loaded: {words} words, {chars} chars, {len(chunks)} TTS chunks")

    if args.dry_run:
        print(f"[INFO] --dry-run: stopping before Sarvam API call.")
        for i, ch in enumerate(chunks[:3], 1):
            print(f"  chunk {i} ({len(ch)} chars): {ch[:120]}...")
        if len(chunks) > 3:
            print(f"  ... and {len(chunks) - 3} more chunks")
        return

    api_key = load_api_key()
    speech = generate_audio(script_clean, api_key, args.voice, verbose=args.verbose)
    if args.verbose:
        print(f"[INFO] Speech generated: {speech.duration_seconds:.1f}s")

    if not args.no_music:
        speech = add_intro_outro(
            speech,
            ASSETS_DIR / INTRO_FILENAME,
            ASSETS_DIR / OUTRO_FILENAME,
            verbose=args.verbose,
        )

    if not args.no_normalize:
        speech = normalize_loudness(speech)
        if args.verbose:
            print(f"[INFO] Loudness normalized to {TARGET_DBFS} dBFS")

    output_path = date_dir / "audio.mp3"
    backup_existing_output(output_path, args.date)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    speech.export(str(output_path), format="mp3", bitrate="128k")

    duration_min = speech.duration_seconds / 60
    file_kb = output_path.stat().st_size / 1024
    print()
    print(f"OK  Audio written: {output_path}")
    print(f"    Duration:     {duration_min:.1f} min ({speech.duration_seconds:.0f}s)")
    print(f"    File size:    {file_kb:.0f} KB")
    print()
    print(f"Next: upload {output_path.name} to Spotify for Podcasters.")
    print(f"      Paste show notes from {date_dir / 'show-notes.md'} as the episode description.")


if __name__ == "__main__":
    main()
