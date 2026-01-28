#!/usr/bin/env python3
"""EasyPlay: diagrama de atividades com logo sobreposto."""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
DIAGRAM = ROOT / "Activities diagram.png"
LOGO = ROOT / "Screenshot from 2026-01-28 13-58-18.png"
OUTPUT = ROOT / "images" / "easyplay.jpg"

TARGET_WIDTH = 800
TARGET_HEIGHT = 600  # 4/3

def main():
    base = Image.open(DIAGRAM).convert("RGB")
    base = base.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)

    logo = Image.open(LOGO)
    if logo.mode in ("RGBA", "P"):
        logo = logo.convert("RGBA")
    else:
        logo = logo.convert("RGBA")

    # Logo max height ~22% da imagem, proporcional
    max_logo_h = int(TARGET_HEIGHT * 0.22)
    w, h = logo.size
    scale = min(1, max_logo_h / h, TARGET_WIDTH * 0.4 / w)
    new_w, new_h = int(w * scale), int(h * scale)
    logo = logo.resize((new_w, new_h), Image.LANCZOS)

    # Centralizar logo sobre o diagrama
    x = (TARGET_WIDTH - new_w) // 2
    y = (TARGET_HEIGHT - new_h) // 2

    if logo.mode == "RGBA":
        base.paste(logo, (x, y), logo)
    else:
        base.paste(logo, (x, y))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    base.save(OUTPUT, "JPEG", quality=90, optimize=True)
    print(f"Saved: {OUTPUT} ({base.size[0]}x{base.size[1]})")

if __name__ == "__main__":
    main()
