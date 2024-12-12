from collections import deque

with open('12.txt') as f:
    grid = [[c for c in list(line)] for line in f.read().splitlines()]

maxI, maxJ = len(grid), len(grid[0])

# connected components
plots = []
visited = set()
for r, line in enumerate(grid):
    for c, label in enumerate(line):
        if (r, c) in visited: continue
        Q = deque([(r, c)])
        plot = [(r, c)]
        visited.add((r, c))
        while Q:
            i, j = Q.popleft()
            for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if not(-1 < ni < maxI and -1 < nj < maxJ) or (ni, nj) in visited: continue
                if grid[ni][nj] == label:
                    plot.append((ni, nj))
                    Q.append((ni, nj))
                    visited.add((ni, nj))
        plots.append(plot)

total2 = total1 = 0
for positions in plots:
    positions.sort(key=lambda x: (x[0], x[1]))
    area = len(positions)
    corners = 0
    perimeter = 0

    for i, j in positions:
        edges = 0
        neighbours = [1 if (ni, nj) not in positions else 0 for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]]
        perimeter += sum(neighbours)
        betweens = [1 if (ni, nj) not in positions else 0 for ni, nj in [(i-1, j+1), (i+1, j+1), (i+1, j-1), (i-1, j-1)]]
        neighbours += [neighbours[0]]
        for el, next, between in zip(neighbours, neighbours[1:], betweens):
            if el == 1 and next == 1 or el == 0 and next == 0 and between == 1:
                corners += 1
    total1 += area * perimeter
    total2 += area * corners

print('Part 1:', total1)
print('Part 2:', total2)