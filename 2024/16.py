from heapq import heappush, heappop

with open('16.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]

si, sj = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]

dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

Q = [(0, si, sj, 1, [(si, sj)])]
fullPath = []
seen = set()
bestScore = 0
totalTiles = set()

while Q:
    score, i, j, d, path = heappop(Q)

    seen.add((i, j, d))

    if grid[i][j] == 'E':
        if not bestScore:
            print('Part 1:', score)
            bestScore = score
            for (pi, pj) in path:
                if (pi, pj) not in totalTiles:
                    totalTiles.add((pi, pj))

        elif score == bestScore:
            for (pi, pj) in path:
                if (pi, pj) not in totalTiles:
                    totalTiles.add((pi, pj))

    di, dj = dirs[d]

    for (nscore, ni, nj, nd, path) in [(score+1, i+di, j+dj, d, path+[(i+di, j+dj)]), (score+1000, i, j, (d+1)%4, path), (score+1000, i, j, (d-1)%4, path)]:
        if grid[ni][nj] == '#' or (ni, nj, nd) in seen: continue
        heappush(Q, (nscore, ni, nj, nd, path))

print('Part 2:', len(totalTiles))