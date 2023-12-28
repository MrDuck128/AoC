from itertools import combinations
from sympy import symbols, Eq, solve

with open('24.txt') as f:
    data = f.read().splitlines()

mx = my = 200000000000000
Mx = My = 400000000000000

def getLine(stone):
    x1, y1, z1, dx, dy, dz = stone
    M = dy / dx
    B = y1 - M * x1
    return M, B, x1 if dx > 0 else -x1

def checkIntersect(l1, l2):
    m1, b1, sx1 = l1
    m2, b2, sx2 = l2
    if m1 == m2: return 0
    xInter = (b2 - b1) / (m1 - m2)
    if xInter > Mx or xInter < mx: return 0
    if (sx1 > 0 and xInter < sx1) or (sx1 < 0 and xInter > sx1*-1) or (sx2 > 0 and xInter < sx2) or (sx2 < 0 and xInter > sx2*-1): return 0
    yInter = m1 * xInter + b1
    if yInter > My or yInter < my: return 0
    return 1

dots = []
for line in data:
    line = [int(x.strip()) for x in line.replace(' @', ',').split(',')]
    dots.append(line)

lines = [getLine(stone) for stone in dots]

total = 0
for l1, l2 in combinations(lines, 2):
    total += checkIntersect(l1, l2)

print('Part 1:', total)

xr, yr, zr, dxr, dyr, dzr = symbols('xr, yr, zr, dxr, dyr, dzr')

equations = []
for i, (sx, sy, sz, dx, dy, dz) in enumerate(dots):
    equations.append(Eq((xr - sx) * (dy - dyr), (yr - sy) * (dx - dxr)))
    equations.append(Eq((yr - sy) * (dz - dzr), (zr - sz) * (dy - dyr)))
    if i == 3:
        break

(ans, ) = [sol for sol in solve(equations)]
print('Part 2:', ans[xr] + ans[yr] + ans[zr])