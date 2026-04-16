import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np
from collections import deque

logo_dir = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\img\logo'

def remove_bg_grow_from_green(path, green_threshold=80, grow_dark_limit=160):
    """
    Two-step approach:
    1. Seed from clearly-green pixels (G > R*1.4 AND G > green_threshold).
    2. BFS outward: expand to neighbouring pixels as long as they are
       'logo-like' (not neutral gray, AND not too bright/flat).
       Stop expanding through obviously neutral-gray background pixels.
    Everything unreached = background → transparent.

    grow_dark_limit: maximum brightness to allow growing into (dark logo pixels).
                     Bright neutral pixels (the medium-gray checkerboard) stop growth.
    """
    img = Image.open(path).convert('RGBA')
    data = np.array(img, dtype=np.int32)
    h, w = data.shape[:2]
    r_ch, g_ch, b_ch = data[...,0], data[...,1], data[...,2]

    # ── Seed mask: definitely green logo pixels ───────────────────────────────
    green_seed = (
        (g_ch > green_threshold) &
        (g_ch.astype(float) > r_ch * 1.35) &
        (g_ch.astype(float) > b_ch * 1.35)
    )
    print(f'  Green seed pixels: {green_seed.sum():,}')

    # ── BFS grow from seeds ───────────────────────────────────────────────────
    def is_neutral(y, x):
        """True = obvious background (neutral gray or light), don't grow through it."""
        r, g, b = int(r_ch[y,x]), int(g_ch[y,x]), int(b_ch[y,x])
        diff = max(abs(r-g), abs(r-b), abs(g-b))
        brightness = max(r, g, b)
        # neutral gray (checkerboard) or bright patch = background
        return diff < 18 and brightness > 30

    kept = np.zeros((h, w), dtype=bool)
    queue = deque()
    ys, xs = np.where(green_seed)
    for y, x in zip(ys.tolist(), xs.tolist()):
        if not kept[y, x]:
            kept[y, x] = True
            queue.append((y, x))

    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < h and 0 <= nx < w and not kept[ny,nx]:
                # Don't cross obviously neutral-gray background pixels
                if is_neutral(ny, nx):
                    continue
                # Don't grow into very bright neutral patches
                if int(data[ny,nx,0]) > 200 and int(data[ny,nx,1]) > 200 and int(data[ny,nx,2]) > 200:
                    continue
                kept[ny, nx] = True
                queue.append((ny, nx))

    print(f'  Logo pixels kept: {kept.sum():,}')
    print(f'  Background pixels removed: {(~kept).sum():,}')

    result = data.astype(np.uint8)
    result[~kept, 3] = 0

    out = Image.fromarray(result, 'RGBA')
    bbox = out.getbbox()
    print(f'  Bbox: {bbox}')
    return out.crop(bbox) if bbox else out


print('Processing...')
icon = remove_bg_grow_from_green(
    os.path.join(logo_dir, 'logo-nextiweb-lumiere.png'),
    green_threshold=80,
    grow_dark_limit=160
)

# Save at 2x retina
iw, ih = icon.size
save_h = 96
save_w = int(iw * save_h / ih)
icon_rs = icon.resize((save_w, save_h), Image.LANCZOS)
print(f'  Output: {save_w}x{save_h}  (display {save_w//2}x{save_h//2})')

for name in ['logo-nextiweb-dark', 'logo-nextiweb-light', 'logo-nextiweb-transparent']:
    icon_rs.save(os.path.join(logo_dir, f'{name}.png'))
    icon_rs.save(os.path.join(logo_dir, f'{name}.webp'), 'WEBP', quality=92)
    kb = os.path.getsize(os.path.join(logo_dir, f'{name}.webp')) // 1024
    print(f'  {name}.webp  {kb}KB')

print(f'\nHTML: width="{save_w//2}" height="{save_h//2}"')
print('Done.')
