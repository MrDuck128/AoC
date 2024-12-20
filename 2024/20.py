from collections import deque
from itertools import combinations

with open('20.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]

si, sj = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]

maxI, maxJ = len(grid), len(grid[0])

Q = deque([(si, sj, 0)])
distances = {(si, sj): (0, -1)}
seen = {(si, sj)}
minT = -1

while Q:
    i, j, t = Q.popleft()

    if grid[i][j] == 'E':
        minT = t

    for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
        if grid[ni][nj] == '#': continue
        if (ni, nj) in seen: continue

        Q.append((ni, nj, t+1))
        distances[(ni, nj)] = (t+1, -1)
        seen.add((ni, nj))

for k, (s, _) in distances.items():
    distances[k] = (s, minT-s)

def count(cheatLen):
    total = 0
    for (i, j), (ii, jj) in combinations(distances, 2):
        dist = abs(i-ii)+abs(j-jj)
        if dist <= cheatLen:
            seconds = distances[(i, j)][0] + dist + distances[(ii, jj)][1]
            if seconds < minT and minT - seconds > 99:
                total += 1
    return total

print('Part 1:', count(2))
print('Part 2:', count(20))