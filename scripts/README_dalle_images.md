# Chapter illustrations via DALL·E

Prepared assets:
- `books/ai_about_ai/images/dalle_prompts.md` (25 EN prompts)
- `books/ai_about_ai_ru/images/dalle_prompts.md` (25 RU prompts)
- `scripts/generate_chapter_images_dalle.py`

## Generate EN images
```bash
pip install openai
export OPENAI_API_KEY=... 
python scripts/generate_chapter_images_dalle.py --lang en
```

## Generate RU images
```bash
python scripts/generate_chapter_images_dalle.py --lang ru
```

Outputs will be written as:
- `books/ai_about_ai/images/01.png ... 25.png`
- `books/ai_about_ai_ru/images/01.png ... 25.png`
