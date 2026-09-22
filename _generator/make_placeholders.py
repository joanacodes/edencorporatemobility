# Génère des images provisoires (dégradés abstraits aux couleurs de la marque) pour chaque emplacement du manifeste.
# Remplacez-les par les vraies photos en gardant le même nom de fichier. Usage : python3 make_placeholders.py
import random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
from images import IMAGES

PAL = {
    "dark":  [(30, 75, 58), (19, 36, 32), (42, 102, 80), (216, 229, 219), (185, 138, 58)],
    "light": [(245, 245, 241), (216, 229, 219), (234, 234, 226), (185, 138, 58), (42, 102, 80)],
    "mid":   [(42, 102, 80), (216, 229, 219), (245, 245, 241), (185, 138, 58), (30, 75, 58)],
}
OUT = Path(__file__).resolve().parent / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

def make(w, h, seed, pal):
    rnd = random.Random(seed)
    sw, sh = w // 10, h // 10
    base = Image.new("RGB", (sw, sh), pal[0])
    d = ImageDraw.Draw(base)
    for i in range(7):
        c = pal[rnd.randrange(1, len(pal))] if i else pal[1]
        r = rnd.randint(sw // 4, sw // 2)
        x = rnd.randint(-r // 2, sw - r // 2); y = rnd.randint(-r // 2, sh - r // 2)
        d.ellipse([x, y, x + r, y + int(r * rnd.uniform(0.6, 1.1))], fill=c)
    base = base.filter(ImageFilter.GaussianBlur(sw // 5))
    img = base.resize((w, h), Image.BICUBIC)
    noise = Image.effect_noise((w, h), 18).convert("L")
    img = Image.blend(img, Image.merge("RGB", (noise, noise, noise)), 0.05)
    return img

for i, it in enumerate(IMAGES):
    w, h = it["size"]
    make(w, h, 100 + i, PAL[it["pal"]]).save(OUT / it["file"], "JPEG", quality=80, optimize=True, progressive=True)
print("placeholders:", len(IMAGES), "→", OUT)
