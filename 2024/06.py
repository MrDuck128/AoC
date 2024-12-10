with open('06.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]

(si, sj) = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '^'][0]

#           up,         right,      down,       left
facing = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
jumpMap = {}

def walk(grid, i, j, f):
    sameJumps = {(i, j, f)}
    while True:
        ni = i + facing[f][0]
        nj = j + facing[f][1]

        if not (-1 < ni < len(grid) and -1 < nj < len(grid[0])):
            jumpMap[(i, j, f)] = (ni, nj, -9)
            for (si, sj, sf) in sameJumps:
                jumpMap[(si, sj, sf)] = (ni, nj, -9)
            break

        if grid[ni][nj] == '#':
            f = (f + 1) % 4
            for (si, sj, sf) in sameJumps:
                jumpMap[(si, sj, sf)] = (i, j, f)
            break

        if (ni, nj, f) not in sameJumps:
            sameJumps.add((ni, nj, f))

        i, j = ni, nj

for i in range(len(grid)):
    for j in range(len(grid[0])):
        for f in range(4):
            if (i, j, f) in jumpMap: continue
            walk(grid, i, j, f)

def part1(grid, i, j, f):
    visited = {(i, j)}
    while True:
        ni = i + facing[f][0]
        nj = j + facing[f][1]

        if not (-1 < ni < len(grid) and -1 < nj < len(grid[0])):
            return visited

        if grid[ni][nj] == '#':
            f = (f + 1) % 4
            continue

        if (ni, nj) not in visited:
            visited.add((ni, nj))

        i, j = ni, nj

visited = part1(grid, si, sj, 0)
print('Part 1:', len(visited))

def checkLoop(i, j):
    src = (si, sj, 0)
    positions = {src}
    samePlace = True if (i, j) == (si, sj) else False
    while True:
        dst = jumpMap[src]
        if samePlace:
            src = dst
            samePlace = False

        elif i == src[0] and min(src[1], dst[1]) <= j <= max(src[1], dst[1]):
            if src[2] == 1:
                src = (i, j-1, 2)
            elif src[2] == 3:
                src = (i, j+1, 0)
        elif j == src[1] and min(src[0], dst[0]) <= i <= max(src[0], dst[0]):
            if src[2] == 0:
                src = (i+1, j, 1)
            elif src[2] == 2:
                src = (i-1, j, 3)
            
        else:
            if dst[2] == -9: return 0
            src = dst

        if src in positions:
            return 1
        positions.add(src)

print('Part 2:', sum(checkLoop(i, j) for (i, j) in visited))