"""Cover the Gemini watermark sparkle in the bottom-right corner of each comic panel.
Approach: copy a clean patch from immediately to the left of the corner (same vertical band)
and paste it over where the star sits. Comic backgrounds at the bottom edge are usually
uniform enough (floor, ground, wall) that a left-shifted patch is invisible.
"""
from PIL import Image
from pathlib import Path

ASSET_DIR = Path(__file__).parent / "assets"
PANELS = [f"comic1-{i}.png" for i in range(1, 7)]

for name in PANELS:
    path = ASSET_DIR / name
    img = Image.open(path).convert("RGB")
    w, h = img.size

    # patch covers about 8% of width/height in the bottom-right
    pw = max(80, int(w * 0.08))
    ph = max(80, int(h * 0.08))

    # source patch: immediately to the LEFT of the star, same vertical band
    src_box = (w - 3 * pw, h - ph, w - 2 * pw, h)
    sample = img.crop(src_box)

    # paste over the corner (bottom-right)
    img.paste(sample, (w - pw, h - ph))

    img.save(path, optimize=True)
    print(f"cleaned {name}: patch {pw}x{ph} at ({w-pw},{h-ph})")
