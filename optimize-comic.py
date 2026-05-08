"""Resize + re-encode comic panels to drop page weight.

For each comic1-N.png:
  - Resize to max 1200px on the long side (display target is ~520px, plenty of headroom)
  - Save optimized PNG (lossless from the resized source, max compression)
  - Save WebP at quality 90 (imperceptibly lossy at display size, ~10x smaller than PNG)

After this script runs, the HTML should use <picture> with the WebP source first
and the PNG as the fallback for the 1% of clients that don't speak WebP.
"""
from PIL import Image
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"
PANELS = [f"comic1-{i}.png" for i in range(1, 7)]
TARGET_LONG_SIDE = 1200

before_total = 0
after_png_total = 0
after_webp_total = 0

for name in PANELS:
    path = ASSET_DIR / name
    before = path.stat().st_size
    before_total += before

    img = Image.open(path).convert("RGB")
    img.thumbnail((TARGET_LONG_SIDE, TARGET_LONG_SIDE), Image.Resampling.LANCZOS)

    img.save(path, "PNG", optimize=True, compress_level=9)
    after_png = path.stat().st_size
    after_png_total += after_png

    webp_path = path.with_suffix(".webp")
    img.save(webp_path, "WEBP", quality=90, method=6)
    after_webp = webp_path.stat().st_size
    after_webp_total += after_webp

    def k(b):
        return f"{b // 1024}KB"
    print(f"{name}: {k(before)} -> PNG {k(after_png)} | WebP {k(after_webp)} ({img.size[0]}x{img.size[1]})")

def m(b):
    return f"{b / 1024 / 1024:.2f}MB"
print(f"\nTOTAL: {m(before_total)} -> PNG {m(after_png_total)} | WebP {m(after_webp_total)}")
