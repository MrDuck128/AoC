from itertools import combinations
from shapely.geometry import Polygon, box

with open('09.txt') as f:
    coords = [tuple(map(int, row.split(','))) for row in f.read().splitlines()]

shape = Polygon(coords)
area1, area2 = 0, 0
for enum, ((ax, ay), (bx, by)) in enumerate(combinations(coords, 2)):
    rectArea = (abs(ax - bx) + 1) * (abs(ay - by) + 1)

    area1 = max(area1, rectArea)

    if box(ax, ay, bx, by).within(shape):
        area2 = max(area2, rectArea)

print('Part 1:', area1)
print('Part 2:', area2)