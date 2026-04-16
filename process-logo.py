import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np

logo_dir = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\img\logo'

def extract_green(path):
    img = Image.open(path).convert('RGBA')
    data = np.array(img, dtype=np.int32)
    r, g, b = data[...,0], data[...,1], data[...,2]
    is_green = (g > 90) & (g > r * 1.3) & (g > b * 1.3)
    result = np.zeros_like(data)
    result[is_green] = data[is_green]
    result[is_green, 3] = 255
    icon = Image.fromarray(result.astype(np.uint8), 'RGBA')
    bbox = icon.getbbox()
    print(f'  bbox: {bbox}  green px: {is_green.sum():,}')
    return icon.crop(bbox)

print('Extracting icon...')
icon = extract_green(os.path.join(logo_dir, 'logo-nextiweb-infini-sans texte.png'))

# Save at 2x retina: display 48px height → save 96px
iw, ih = icon.size
ratio = iw / ih
save_h = 96
save_w = int(ratio * save_h)
print(f'  Output size: {save_w}x{save_h}')

icon_rs = icon.resize((save_w, save_h), Image.LANCZOS)

for name in ['logo-nextiweb-dark', 'logo-nextiweb-light', 'logo-nextiweb-transparent']:
    icon_rs.save(os.path.join(logo_dir, f'{name}.png'))
    icon_rs.save(os.path.join(logo_dir, f'{name}.webp'), 'WEBP', quality=92)
    kb = os.path.getsize(os.path.join(logo_dir, f'{name}.webp')) // 1024
    print(f'  {name}.webp  {kb}KB')

print(f'\nDisplay size in HTML: width="{save_w//2}" height="{save_h//2}"')
print('Done.')
