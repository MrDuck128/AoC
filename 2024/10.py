from collections import deque

with open('10.txt') as f:
    grid = [[int(x) for x in list(line)] for line in f.read().splitlines()]

maxI, maxJ = len(grid), len(grid[0])

trailheads = [(i, j) for i in range(maxI) for j in range(maxJ) if grid[i][j] == 0]

total1 = total2 = 0
for (i, j) in trailheads:
    Q = deque([(i, j)])
    visited = {(i, j)}
    peaks = 0
    peaksVisited = set()

    while Q:
        i, j = Q.popleft()
        for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if not(-1 < ni < maxI and -1 < nj < maxJ): continue
            if grid[ni][nj] != grid[i][j] + 1: continue

            if grid[ni][nj] == 9:
                peaksVisited.add((ni, nj))
                peaks += 1
            else:
                Q.append((ni, nj))

    total1 += len(peaksVisited)
    total2 += peaks

print('Part 1:', total1)
print('Part 2:', total2)
