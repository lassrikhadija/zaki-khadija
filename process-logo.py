import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont
import numpy as np

logo_dir   = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\img\logo'
icons_dir  = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\icons'
FONT_PATH  = r'C:\Windows\Fonts\arialbd.ttf'

def extract_green_icon(path, green_min_g=90, green_ratio=1.3):
    """Keep only green pixels, everything else → transparent."""
    img = Image.open(path).convert('RGBA')
    data = np.array(img, dtype=np.int32)
    r, g, b = data[...,0], data[...,1], data[...,2]

    # Green pixel: G dominant, G > green_min_g, G > R*ratio, G > B*ratio
    is_green = (g > green_min_g) & (g > r * green_ratio) & (g > b * green_ratio)

    result = np.zeros_like(data)
    result[is_green] = data[is_green]
    result[is_green, 3] = 255  # fully opaque

    icon = Image.fromarray(result.astype(np.uint8), 'RGBA')
    bbox = icon.getbbox()
    print(f'  Green pixels: {is_green.sum():,}  bbox: {bbox}')
    return icon.crop(bbox) if bbox else icon

# ── 1. Extract icon ───────────────────────────────────────────────────────────
print('Extracting icon from logo...')
icon = extract_green_icon(os.path.join(logo_dir, 'logo-nextiweb-infini.png'))

print('Extracting icon from favicon...')
fav_icon = extract_green_icon(os.path.join(logo_dir, 'favicon-nextiweb-infini.png'))

# ── 2. Build logo: icon + "NEXTIWEB" text ─────────────────────────────────────
CANVAS_W, CANVAS_H = 560, 140
ICON_H   = 100
GAP      = 20
FONT_SZ  = 68

iw, ih = icon.size
icon_w  = int(iw * ICON_H / ih)
icon_rs = icon.resize((icon_w, ICON_H), Image.LANCZOS)

font = ImageFont.truetype(FONT_PATH, FONT_SZ)
dummy = Image.new('RGBA', (1,1))
d = ImageDraw.Draw(dummy)
bbox_t = d.textbbox((0,0), 'NEXTIWEB', font=font)
text_w  = bbox_t[2] - bbox_t[0]
text_h  = bbox_t[3] - bbox_t[1]

total_w  = icon_w + GAP + text_w
offset_x = (CANVAS_W - total_w) // 2
icon_y   = (CANVAS_H - ICON_H) // 2
text_y   = (CANVAS_H - text_h) // 2 - bbox_t[1]

def make_logo(text_color):
    canvas = Image.new('RGBA', (CANVAS_W, CANVAS_H), (0,0,0,0))
    canvas.paste(icon_rs, (offset_x, icon_y), icon_rs)
    draw = ImageDraw.Draw(canvas)
    draw.text((offset_x + icon_w + GAP, text_y), 'NEXTIWEB', font=font, fill=text_color)
    return canvas

logo_dark  = make_logo((255, 255, 255, 255))   # white text for dark bg
logo_light = make_logo((28,  40,  58,  255))   # dark navy text for light bg

print('\nSaving logos...')
SAVE_W, SAVE_H = 280, 70
for name, img in [('logo-nextiweb-dark',        logo_dark),
                  ('logo-nextiweb-light',        logo_light),
                  ('logo-nextiweb-transparent',  logo_light)]:
    out = img.resize((SAVE_W, SAVE_H), Image.LANCZOS)
    out.save(os.path.join(logo_dir, f'{name}.png'))
    out.save(os.path.join(logo_dir, f'{name}.webp'), 'WEBP', quality=92)
    kb = os.path.getsize(os.path.join(logo_dir, f'{name}.webp')) // 1024
    print(f'  {name}.webp  {kb}KB')

# ── 3. Favicon ────────────────────────────────────────────────────────────────
print('\nCreating favicon...')
fw, fh = fav_icon.size
side = max(fw, fh)
sq = Image.new('RGBA', (side, side), (0,0,0,0))
sq.paste(fav_icon, ((side-fw)//2, (side-fh)//2))

fav_32 = sq.resize((32, 32), Image.LANCZOS)
fav_32.save(os.path.join(icons_dir, 'favicon.ico'), format='ICO', sizes=[(16,16),(32,32),(64,64)])
fav_32.save(os.path.join(icons_dir, 'favicon-32.png'))
print('  favicon.ico saved')

print('\nAll done.')
