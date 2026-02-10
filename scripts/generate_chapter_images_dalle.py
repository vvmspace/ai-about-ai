#!/usr/bin/env python3
"""
Generate one DALL·E image per chapter prompt file.
Requires: OPENAI_API_KEY in environment and openai>=1.0.0

Usage:
  python scripts/generate_chapter_images_dalle.py --lang en
  python scripts/generate_chapter_images_dalle.py --lang ru
"""

from __future__ import annotations

import argparse
import base64
import os
from pathlib import Path


def parse_prompts(path: Path):
    items = []
    for line in path.read_text().splitlines():
        if not line.startswith("- "):
            continue
        # split robustly around markers
        try:
            prompt = line.split('Prompt: "', 1)[1].split('" |', 1)[0]
            output = line.rsplit('`', 2)[1]
        except Exception:
            try:
                prompt = line.split('Промпт: "', 1)[1].split('" |', 1)[0]
                output = line.rsplit('`', 2)[1]
            except Exception:
                continue
        items.append((prompt, Path(output)))
    return items


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=["en", "ru"], required=True)
    parser.add_argument("--model", default="gpt-image-1")
    parser.add_argument("--size", default="1536x1024")
    args = parser.parse_args()

    if "OPENAI_API_KEY" not in os.environ:
        raise SystemExit("OPENAI_API_KEY is not set")

    try:
        from openai import OpenAI
    except Exception as e:
        raise SystemExit(f"Install dependency first: pip install openai. Details: {e}")

    prompt_file = (
        Path("books/ai_about_ai/images/dalle_prompts.md")
        if args.lang == "en"
        else Path("books/ai_about_ai_ru/images/dalle_prompts.md")
    )
    items = parse_prompts(prompt_file)
    if not items:
        raise SystemExit(f"No prompts parsed from {prompt_file}")

    client = OpenAI()

    for i, (prompt, out) in enumerate(items, start=1):
        out.parent.mkdir(parents=True, exist_ok=True)
        print(f"[{i}/{len(items)}] Generating {out}...")
        resp = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.size,
        )
        b64 = resp.data[0].b64_json
        out.write_bytes(base64.b64decode(b64))

    print("Done.")


if __name__ == "__main__":
    main()
