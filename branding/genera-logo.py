import math, sys, os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
NAVY, TEAL, TEAL_D, WHITE = "#163E73", "#2EC4A0", "#14866C", "#FFFFFF"

font = instantiateVariableFont(TTFont("/usr/share/fonts/opentype/cantarell/Cantarell-VF.otf"), {"wght": 700})
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
upm = font["head"].unitsPerEm

def text_paths(s, size, x0, baseline, tracking=0):
    sc = size / upm; x = x0; out = []
    for ch in s:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, x, baseline)))
        out.append(pen.getCommands())
        x += hmtx[g][0] * sc + tracking
    return " ".join(out), x - tracking

def arc(cx, cy, r, a0=-135, a1=-45):
    p = lambda a: (cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1)
    return f"M{x0:.2f} {y0:.2f}A{r} {r} 0 0 1 {x1:.2f} {y1:.2f}"

def mark(tile=NAVY, page=WHITE, signal=TEAL):
    cx, cy = 128, 126
    arcs = "".join(f'<path d="{arc(cx, cy, r)}"/>' for r in (30, 52, 74))
    return f'''<rect width="256" height="256" rx="56" fill="{tile}"/>
  <g fill="none" stroke="{signal}" stroke-width="14" stroke-linecap="round">{arcs}</g>
  <circle cx="{cx}" cy="{cy}" r="10" fill="{signal}"/>
  <g fill="{page}">
    <path d="M121 204C102 191 78 186 52 189V141C78 137 102 142 121 154Z"/>
    <path d="M135 204C154 191 178 186 204 189V141C178 137 154 142 135 154Z"/>
  </g>'''

def svg(w, h, body, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t">
  <title id="t">{title}</title>
  {body}
</svg>
'''

open(f"{OUT}/eduwisp-mark.svg","w").write(svg(256,256,mark(),"EduWISP"))
open(f"{OUT}/eduwisp-mark-mono.svg","w").write(svg(256,256,mark(tile="#000000",page="#FFFFFF",signal="#FFFFFF"),"EduWISP"))

def lockup(edu, wisp, tile=NAVY, page=WHITE, signal=TEAL, name="", bg=None):
    size, gap = 150, 40
    p1, x1 = text_paths("Edu", size, 256+gap, 0)
    p2, x2 = text_paths("WISP", size, x1 + 2, 0)
    # centra verticalmente il testo sul marchio usando l'altezza delle maiuscole
    bp = BoundsPen(gs); gs[cmap[ord("E")]].draw(bp); cap = bp.bounds[3] * size / upm
    base = 128 + cap/2
    p1, _ = text_paths("Edu", size, 256+gap, base)
    p2, _ = text_paths("WISP", size, x1 + 2, base)
    w = math.ceil(x2) + 8
    bgr = f'<rect width="{w}" height="256" fill="{bg}"/>' if bg else ""
    body = f'''{bgr}<g>{mark(tile, page, signal)}</g>
  <path fill="{edu}" d="{p1}"/>
  <path fill="{wisp}" d="{p2}"/>'''
    open(f"{OUT}/{name}","w").write(svg(w,256,body,"EduWISP"))

lockup(TEAL_D, NAVY, name="eduwisp-logo.svg")
lockup(TEAL, WHITE, tile="#FFFFFF", page=NAVY, signal=TEAL_D, name="eduwisp-logo-dark.svg")
print("ok")
