import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import numpy as np
from collections import deque

logo_dir = r'C:\Users\Chaki\Downloads\e-commerce-khadija\Khadija marketing\Projet-khadija\projet_Nextiweb\zaki-khadija\assets\img\logo'

def flood_remove_bg(path, tolerance=28):
    """
    Flood-fill from all 4 corners to find background pixels,
    then make them transparent. Stops at logo content.
    """
    img = Image.open(path).convert('RGBA')
    data = np.array(img, dtype=np.int32)
    h, w = data.shape[:2]
    r, g, b = data[...,0], data[...,1], data[...,2]

    # Sample background color from multiple corner points
    corner_pts = [(0,0),(0,w-1),(h-1,0),(h-1,w-1),
                  (0,w//2),(h-1,w//2),(h//2,0),(h//2,w-1),
                  (5,5),(5,w-6),(h-6,5),(h-6,w-6)]
    bg_r = int(np.median([data[y,x,0] for y,x in corner_pts]))
    bg_g = int(np.median([data[y,x,1] for y,x in corner_pts]))
    bg_b = int(np.median([data[y,x,2] for y,x in corner_pts]))
    print(f'  Background color sampled: RGB({bg_r},{bg_g},{bg_b})')

    def is_bg(y, x):
        dr = abs(int(data[y,x,0]) - bg_r)
        dg = abs(int(data[y,x,1]) - bg_g)
        db = abs(int(data[y,x,2]) - bg_b)
        return (dr + dg + db) < tolerance * 3

    # BFS flood fill from all edge pixels
    visited = np.zeros((h, w), dtype=bool)
    queue = deque()

    # Seed from all border pixels that match background
    for x in range(w):
        for y in [0, h-1]:
            if not visited[y,x] and is_bg(y,x):
                visited[y,x] = True
                queue.append((y,x))
    for y in range(h):
        for x in [0, w-1]:
            if not visited[y,x] and is_bg(y,x):
                visited[y,x] = True
                queue.append((y,x))

    while queue:
        cy, cx = queue.popleft()
        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = cy+dy, cx+dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny,nx] and is_bg(ny,nx):
                visited[ny,nx] = True
                queue.append((ny,nx))

    print(f'  Background pixels removed: {visited.sum():,}')

    result = data.astype(np.uint8)
    result[visited, 3] = 0

    out = Image.fromarray(result, 'RGBA')
    bbox = out.getbbox()
    print(f'  Bbox: {bbox}')
    return out.crop(bbox) if bbox else out

print('Processing...')
icon = flood_remove_bg(os.path.join(logo_dir, 'logo-nextiweb-lumiere.png'), tolerance=30)

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
