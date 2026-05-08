"""Generate favicon set from a tight face crop of close.png (the modern-Bob portrait).
Emits favicon.ico (multi-res), favicon-32/192/512.png, and apple-touch-icon.png (180).
"""
from PIL import Image
from pathlib import Path

src = Path("c:/Agents/Mindy/output/RebootPilot/assets/close.png")
out = Path(__file__).parent / "assets"

img = Image.open(src).convert("RGBA")
# Tight square crop on Bob's face: hair top -> upper torso, full mustache + shades visible
crop_box = (200, 70, 760, 630)
face = img.crop(crop_box)

png_sizes = [
    ("favicon-32.png", 32),
    ("favicon-192.png", 192),
    ("favicon-512.png", 512),
    ("apple-touch-icon.png", 180),
]
for name, size in png_sizes:
    resized = face.resize((size, size), Image.Resampling.LANCZOS)
    resized.save(out / name, "PNG", optimize=True)
    print(f"{name}: {size}x{size}")

# multi-resolution .ico for legacy browsers
face.save(out / "favicon.ico", "ICO", sizes=[(16, 16), (32, 32), (48, 48)])
print("favicon.ico")
