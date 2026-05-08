"""Remove the (incorrectly placed) US flag patch from Murillo's LEFT shoulder in panel 1.
Sample a clean strip of camo from his lower torso and paste it over the flag.
"""
from PIL import Image
from pathlib import Path

path = Path(__file__).parent / "assets" / "comic1-1.png"
img = Image.open(path).convert("RGB")
w, h = img.size  # 2048, 2048

# Flag patch bounds (estimated from visual inspection of the panel).
# Murillo's left shoulder is on the right side of the image.
flag_box = (1780, 900, 1920, 1080)  # left, top, right, bottom

# Sample a clean piece of his uniform camo from below the patches and name tape.
# Murillo's lower torso / abdomen — pure camo, same lighting/shading.
fb_w = flag_box[2] - flag_box[0]
fb_h = flag_box[3] - flag_box[1]
sample_box = (1500, 1320, 1500 + fb_w, 1320 + fb_h)
sample = img.crop(sample_box)

img.paste(sample, (flag_box[0], flag_box[1]))
img.save(path, optimize=True)
print(f"patched flag in comic1-1.png: {fb_w}x{fb_h} at ({flag_box[0]},{flag_box[1]})")
