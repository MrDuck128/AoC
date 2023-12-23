with open('23.txt') as f:
    grid = [[*line] for line in f.read().splitlines()]

si, sj = 0, grid[0].index('.')
ei, ej = len(grid)-1, grid[len(grid)-1].index('.')

dirs = {'>': [(0, 1)], 'v': [(1, 0)], '<': [(0, -1)],  '^': [(-1, 0)],  '.': [(0, 1), (1, 0), (0, -1), (-1, 0)]}

splits = [(si, sj), (ei, ej)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            paths = 0
            for di, dj in dirs['.']:
                if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]) and grid[i+di][j+dj] in dirs:
                    paths += 1
            if paths > 2:
                splits.append((i, j))

def makePaths(part):
    paths = {x: {} for x in splits}
    for si, sj in splits:
        Q = [(si, sj, 0)]
        seen = set()

        while Q:
            i, j, steps = Q.pop(0)

            if (i, j) in seen:
                continue
            seen.add((i, j))

            if (i, j) in splits and steps != 0:
                paths[(si, sj)][(i, j)] = steps
                continue
            
            if part == 1:
                for di, dj in dirs[grid[i][j]]:
                    if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]) and grid[i+di][j+dj] in dirs:
                        Q.append((i+di, j+dj, steps+1))
            elif part == 2:
                for di, dj in dirs['.']:
                    if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]) and grid[i+di][j+dj] in dirs:
                        Q.append((i+di, j+dj, steps+1))
    return paths

def dfs(start, steps, seen):
    if start == (ei, ej):
        fullPaths.append(steps)

    currSeen = seen.copy()
    currSeen.add(start)

    for node, step in paths[start].items():
        if node not in currSeen:
            dfs(node, steps+step, currSeen)

fullPaths = []
seen = set()
paths = makePaths(1)
dfs((0, grid[0].index('.')), 0, seen)
print('Part 1:', max(fullPaths))

fullPaths = []
seen = set()
paths = makePaths(2)
dfs((0, grid[0].index('.')), 0, seen)
print('Part 2:', max(fullPaths))