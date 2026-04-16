import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np

logo_dir = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\img\logo'

print('Processing logo-nextiweb-lumiere.png...')
src = Image.open(os.path.join(logo_dir, 'logo-nextiweb-lumiere.png')).convert('RGBA')
data = np.array(src, dtype=np.int32)
r, g, b, a = data[...,0], data[...,1], data[...,2], data[...,3]

# Remove only pure checkerboard squares (neutral gray, NOT the dark logo shadow)
# Checkerboard: R≈G≈B AND mid-bright (120-220) AND NOT dark green content
is_neutral  = (np.abs(r-g) <= 10) & (np.abs(g-b) <= 10)
is_midgray  = ((r+g+b)//3).astype(np.int32)
is_checker  = is_neutral & (is_midgray >= 120) & (is_midgray <= 215)

# Protect dark logo shadow: pixels where green is dominant (even slightly)
# or where it's very dark (logo shadow/glow area)
is_logo_dark = ((r+g+b)//3 < 80)   # very dark = logo shadow
is_green_tint = (g.astype(float) > r * 1.05)  # slightly green = logo content

keep = ~is_checker | is_logo_dark | is_green_tint

result = data.astype(np.uint8)
result[~keep, 3] = 0

icon = Image.fromarray(result, 'RGBA')
bbox = icon.getbbox()
print(f'  bbox: {bbox}')
icon_cropped = icon.crop(bbox) if bbox else icon

# Save at 2x retina — 96px height
iw, ih = icon_cropped.size
save_h = 96
save_w = int(iw * save_h / ih)
icon_rs = icon_cropped.resize((save_w, save_h), Image.LANCZOS)
print(f'  Output: {save_w}x{save_h}  (display {save_w//2}x{save_h//2})')

for name in ['logo-nextiweb-dark', 'logo-nextiweb-light', 'logo-nextiweb-transparent']:
    icon_rs.save(os.path.join(logo_dir, f'{name}.png'))
    icon_rs.save(os.path.join(logo_dir, f'{name}.webp'), 'WEBP', quality=92)
    kb = os.path.getsize(os.path.join(logo_dir, f'{name}.webp')) // 1024
    print(f'  {name}.webp  {kb}KB')

print(f'\nHTML: width="{save_w//2}" height="{save_h//2}"')
print('Done.')
