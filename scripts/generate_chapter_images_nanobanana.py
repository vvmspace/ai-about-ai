#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, base64
from pathlib import Path
from typing import Iterable

MODEL_DEFAULT = "gemini-2.5-flash-image-preview"

def chapter_files(lang:str)->Iterable[Path]:
    base=Path("books/ai_about_ai" if lang=="en" else "books/ai_about_ai_ru")
    return [p for p in sorted(base.glob('[0-9][0-9]_*.md')) if not p.name.startswith('00_')]

def title_of(path:Path)->str:
    return path.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()

def prompt_for(title:str,lang:str)->str:
    if lang=='en':
        return f"Create a cinematic editorial illustration for a book chapter titled '{title}'. Modern 2026 AI workplace, human + AI collaboration, clean composition, high detail, soft dramatic lighting, optimistic but grounded mood, no text, no logos, no watermark."
    return f"Создай кинематографичную редакционную иллюстрацию для главы книги '{title}'. Современная AI-рабочая среда 2026 года, сотрудничество человека и ИИ, чистая композиция, высокий уровень деталей, мягкий драматичный свет, оптимистичный, но приземлённый тон, без текста, логотипов и водяных знаков."

def out_path(p:Path,lang:str)->Path:
    n=p.name[:2]
    return Path(f"books/ai_about_ai/images/{n}.png" if lang=='en' else f"books/ai_about_ai_ru/images/{n}.png")

def extract_image_bytes(resp)->bytes:
    for cand in getattr(resp,'candidates',[]) or []:
        content=getattr(cand,'content',None)
        for part in (getattr(content,'parts',[]) or []):
            inline=getattr(part,'inline_data',None)
            if inline and getattr(inline,'data',None):
                data=inline.data
                if isinstance(data,bytes): return data
                try: return base64.b64decode(data)
                except Exception: pass
    raise RuntimeError('No image data returned')

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--lang',choices=['en','ru'],required=True)
    ap.add_argument('--model',default=MODEL_DEFAULT)
    ap.add_argument('--dry-run',action='store_true')
    args=ap.parse_args()

    key=os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not key:
        raise SystemExit('Missing GEMINI_API_KEY/GOOGLE_API_KEY in environment')

    files=chapter_files(args.lang)
    if args.dry_run:
        for p in files:
            print(f"{p.name} -> {out_path(p,args.lang)} :: {title_of(p)}")
        return 0

    from google import genai
    client=genai.Client(api_key=key)

    for i,p in enumerate(files,1):
        out=out_path(p,args.lang)
        out.parent.mkdir(parents=True,exist_ok=True)
        print(f"[{i}/{len(files)}] {p.name} -> {out}")
        resp=client.models.generate_content(
            model=args.model,
            contents=prompt_for(title_of(p),args.lang),
            config={"response_modalities":["TEXT","IMAGE"],"image_config":{"aspect_ratio":"16:9"}},
        )
        out.write_bytes(extract_image_bytes(resp))
    print('Done')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
