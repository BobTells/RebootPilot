"""Optimize the hero banner: WebP at q90 + re-save PNG with max compression.
The native size (1920x819) is already a good display match, so no resize."""
from PIL import Image
from pathlib import Path

src = Path(__file__).parent / "assets" / "brain-droppings-6-banner.png"
before = src.stat().st_size
img = Image.open(src).convert("RGB")
img.save(src, "PNG", optimize=True, compress_level=9)
img.save(src.with_suffix(".webp"), "WEBP", quality=90, method=6)
after_png = src.stat().st_size
after_webp = src.with_suffix(".webp").stat().st_size
print(f"hero: {before//1024}KB -> PNG {after_png//1024}KB | WebP {after_webp//1024}KB ({img.size[0]}x{img.size[1]})")
