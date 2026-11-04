"""Generate palouse.svg, the line drawing of rolling Palouse hills used on the home page.

Run from the repo root:  python3 tools/palouse_art.py
"""

import math
import random

WIDTH, HEIGHT = 1200, 240
STEP = 50
random.seed(7)

LIGHT = {"line": "#9a8f7c", "fill": "#f6f4ef", "sun": "#c9a66b"}
DARK = {"line": "#6f685d", "fill": "#141412", "sun": "#8a7550"}


def ridge(base, amp, waves):
    """Points along a hill line: a base height plus a few overlapping sine waves."""
    pts = []
    for x in range(-2 * STEP, WIDTH + 3 * STEP, STEP):
        y = base
        for length, weight, phase in waves:
            y -= amp * weight * math.sin(2 * math.pi * x / length + phase)
        pts.append((x, y))
    return pts


def smooth_path(pts):
    """Catmull-Rom spline through pts, written as SVG cubic beziers."""
    d = f"M{pts[0][0]} {pts[0][1]:.0f}"
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.0f} {c1[1]:.0f} {c2[0]:.0f} {c2[1]:.0f} {p2[0]} {p2[1]:.0f}"
    return d


def random_waves(count):
    return [
        (random.uniform(380, 900), random.uniform(0.4, 1.0), random.uniform(0, 2 * math.pi))
        for _ in range(count)
    ]


# Back to front: (baseline, amplitude, number of crop-row stripes)
layers = [
    (92, 16, 0),
    (122, 22, 0),
    (152, 26, 4),
    (186, 30, 6),
    (222, 32, 8),
]

defs, body = [], []
for i, (base, amp, stripes) in enumerate(layers):
    line = smooth_path(ridge(base, amp, random_waves(3)))
    hill = f"{line}V{HEIGHT + 10}H{-2 * STEP}Z"
    defs.append(f'<path id="r{i}" d="{line}"/>')
    defs.append(f'<clipPath id="c{i}"><path d="{hill}"/></clipPath>')
    body.append(f'<path class="h" d="{hill}"/>')
    if stripes:
        # Crop rows follow the hill's contour and flatten toward the valley.
        rows = "".join(
            f'<use href="#r{i}" transform="translate({k * 4} {base + k * 11}) scale(1 {1 - k * 0.09:.2f}) translate(0 {-base})"/>'
            for k in range(1, stripes + 1)
        )
        body.append(f'<g class="row" clip-path="url(#c{i})">{rows}</g>')

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" preserveAspectRatio="xMidYMax slice">
<style>
.h{{fill:{LIGHT['fill']};stroke:{LIGHT['line']};stroke-width:1.6}}
.row{{fill:none;stroke:{LIGHT['line']};stroke-width:1;opacity:.55}}
.sun{{fill:none;stroke:{LIGHT['sun']};stroke-width:1.6}}
@media (prefers-color-scheme:dark){{
.h{{fill:{DARK['fill']};stroke:{DARK['line']}}}
.row{{stroke:{DARK['line']}}}
.sun{{stroke:{DARK['sun']}}}
}}
</style>
<defs>{''.join(defs)}</defs>
<circle class="sun" cx="930" cy="62" r="30"/>
{''.join(body)}
</svg>
"""

with open("palouse.svg", "w") as f:
    f.write(svg)
print(f"wrote palouse.svg ({len(svg)} bytes)")
