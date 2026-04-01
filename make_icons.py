from PIL import Image, ImageDraw
import math

def make_icon(size, path):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    
    # Background circle - soft pink
    margin = size * 0.05
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#f9e0e8')
    
    # Draw a heart shape
    cx, cy = size/2, size/2 + size*0.04
    r = size * 0.22
    
    # Heart via bezier approximation using polygon
    points = []
    for t in range(0, 360):
        rad = math.radians(t)
        x = 16 * (math.sin(rad) ** 3)
        y = -(13 * math.cos(rad) - 5 * math.cos(2*rad) - 2 * math.cos(3*rad) - math.cos(4*rad))
        scale = size * 0.028
        points.append((cx + x*scale, cy + y*scale))
    
    draw.polygon(points, fill='#c96b8a')
    img.save(path)
    print(f"Saved {path}")

make_icon(192, '/home/claude/bizim_hikayemiz/icon-192.png')
make_icon(512, '/home/claude/bizim_hikayemiz/icon-512.png')
