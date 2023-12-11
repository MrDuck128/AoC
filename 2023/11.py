import numpy as np

with open('11.txt') as f:
    grid = np.array([[*line] for line in f.read().splitlines()])

emptyI = [i for i in range(len(grid)) if set(grid[i]) == {'.'}]
emptyJ = [j for j in range(len(grid[0])) if set(grid[:, j]) == {'.'}]

galaxies, galaxies2 = [[] for _ in range(2)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i, j] == '#':
            numI = [num for num, eI in enumerate(emptyI) if eI < i]
            numJ = [num for num, eJ in enumerate(emptyJ) if eJ < j]
            galaxies.append((i+len(numI), j+len(numJ)))
            galaxies2.append((i+len(numI)*999_999, j+len(numJ)*999_999))

shortestPaths = shortestPaths2 = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        shortestPaths += abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
        shortestPaths2 += abs(galaxies2[j][0] - galaxies2[i][0]) + abs(galaxies2[j][1] - galaxies2[i][1])

print('Part 1:', shortestPaths)
print('Part 2:', shortestPaths2)