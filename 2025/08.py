from itertools import combinations
from collections import defaultdict
from math import prod

with open('08.txt') as f:
    coords = [tuple(map(int, row.split(','))) for row in f.read().splitlines()]

D = sorted([(((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)/2, (x1, y1, z1), (x2, y2, z2)) for (x1, y1, z1), (x2, y2, z2) in combinations(coords, 2)])
C = defaultdict(set)

def find(x):
    for k, v in C.items():
        if x in v:
            return k
    return 0

for i in range(len(D)):
    d, a, b = D[i]
    ak, bk = find(a), find(b)

    if not ak and not bk:
        C[(max(C) if C else 0)+1] = {a, b}
    elif ak and not bk:
        C[ak].add(b)
    elif bk and not ak:
        C[bk].add(a)
    elif ak and bk and ak != bk:
        C[ak].update(C[bk])
        del C[bk]

    if i == 999:
        print('Part 1:', prod(sorted([len(vals) for vals in C.values()], reverse=True)[:3]))

    if len(next(iter(C.values()))) == len(coords):
        print('Part 2:', a[0]*b[0])
        break