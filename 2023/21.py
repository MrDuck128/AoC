with open('21.txt') as f:
    grid = [[*line] for line in f.read().splitlines()]

size = len(grid)
(sx, sy) = [(i, j) for i in range(size) for j in range(size) if grid[i][j] == 'S'][0]

def bff(si, sj, step, odd, outside):
    seen = {(si, sj)}
    Q = [(si, sj, 0)]
    possible = set()
    if outside:
        possibleOutside = set()

    while Q:
        i, j, s = Q.pop(0)

        if s % 2 == odd:
            possible.add((i, j))

        if outside and s % 2 == odd and s > 65:
            possibleOutside.add((i, j))

        if s == step:
            continue

        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < size and 0 <= nj < size and grid[ni][nj] != '#' and (ni, nj) not in seen:
                Q.append((ni, nj, s+1))
                seen.add((ni, nj))

    if outside:
        return len(possibleOutside)
    return len(possible)

print('Part 1:', bff(sx, sy, 64, 0, 0))

oddIns = bff(sx, sy, 164, 1, 0)
evenIns = bff(sx, sy, 164, 0, 0)
oddOut = bff(sx, sy, 164, 1, 1)
evenOut = bff(sx, sy, 164, 0, 1)

n = (26501365 - (size - 1) // 2) // size
ans = (n+1)**2 * oddIns + n**2 * evenIns - (n+1) * oddOut + n * evenOut

print('Part 2:', ans)