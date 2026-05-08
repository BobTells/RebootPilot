"""Patch out the (incorrectly placed) US flag patch from Murillo's LEFT shoulder
in panel 1 of the comic. Sample clean sleeve material from immediately below the
flag and paste it over the flag location. Re-save both PNG and WebP variants.
"""
from PIL import Image
from pathlib import Path

panel = Path(__file__).parent / "assets" / "comic1-1.png"
img = Image.open(panel).convert("RGB")
w, h = img.size  # 1200x1200

# Flag patch bounds (estimated on the 1200x1200 source).
# Murillo is on the right side of the panel; his LEFT shoulder is on the
# RIGHT side of the image. The flag sits above his name tape.
flag_box = (1030, 530, 1130, 640)
fb_w = flag_box[2] - flag_box[0]
fb_h = flag_box[3] - flag_box[1]

# Sample from immediately below the flag — same arm/sleeve material,
# similar lighting, no patches.
sample_box = (1030, 720, 1030 + fb_w, 720 + fb_h)
sample = img.crop(sample_box)
img.paste(sample, (flag_box[0], flag_box[1]))

img.save(panel, "PNG", optimize=True, compress_level=9)
img.save(panel.with_suffix(".webp"), "WEBP", quality=90, method=6)
print(f"patched flag on Murillo: {fb_w}x{fb_h} at ({flag_box[0]},{flag_box[1]})")
