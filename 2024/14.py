import re

with open('14.txt') as f:
    lines = f.read().splitlines()

robots = {(d, c, b, a): (b, a) for line in lines for a, b, c, d in [map(int, re.findall('-?\\d+', line))]}
h, w = 103, 101

def advanceRobots(robots, step=1):
    for (di, dj, *rest), (i, j) in robots.items():
        robots[(di, dj, *rest)] = ((i+di*step)%h, (j+dj*step)%w)
    return robots

robots = advanceRobots(robots, 100)

q1 = q2 = q3 = q4 = 0
hh, hw = h//2, w//2
for (i, j) in robots.values():
    if i == hh or j == hw: continue
    if i < hh:
        if j < hw: q1 += 1
        else: q2 += 1
    else:
        if j < hw: q3 += 1
        else: q4 += 1

print('Part 1:', q1 * q2 * q3 * q4)

def checkVertical(coords):
    l = 0
    coords = sorted(coords, key=lambda x: (x[1], x[0]))
    for (i, j), (ni, nj) in zip(coords, coords[1:]):
        if l > 10: return 1
        if j == nj and -1 < ni-1 and i == ni-1: l += 1
        else: l = 0
    return 0

for sec in range(101, 10_000):
    robots = advanceRobots(robots)
    if checkVertical(robots.values()): 
        print('Part 2:', sec)
        break