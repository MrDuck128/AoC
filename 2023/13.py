import numpy as np 

with open('13.txt') as f:
    data = f.read().split('\n\n')

def checkGrid(grid, trans, diffs_allowed):
    R = len(grid)
    C = len(grid[0])
    for j in range(C-1):
        middle = C // 2
        check = True
        diffs = 0

        if j < middle:
            for i in range(R):
                if not diffs_allowed:
                    if not np.array_equal(grid[i][:j+1], np.flip(grid[i][j+1:(j+1)*2])):
                        check = False
                        break
                else:
                    diffs += np.sum(grid[i][:j+1] != np.flip(grid[i][j+1:(j+1)*2]))
                    if diffs > diffs_allowed:
                        break
            if diffs_allowed and diffs == diffs_allowed:
                return (j+1)*100 if trans else j+1
            if not diffs_allowed and check:
                return (j+1)*100 if trans else j+1
                
        else:
            for i in range(R):
                if not diffs_allowed:
                    if not np.array_equal(grid[i][(j+1)*2-C:j+1], np.flip(grid[i][j+1:])):
                        check = False
                        break
                else:
                    diffs += np.sum(grid[i][(j+1)*2-C:j+1] != np.flip(grid[i][j+1:]))
                    if diffs > diffs_allowed:
                        break
            if diffs_allowed and diffs == diffs_allowed:
                return (j+1)*100 if trans else j+1
            if not diffs_allowed and check:
                return (j+1)*100 if trans else j+1
    return 0

total = total2 = 0
for grid in data:
    grid = np.array([[*line] for line in grid.splitlines()])

    t = checkGrid(grid, False, 0)
    if t:
        total += t
        continue
    total += checkGrid(grid.T, True, 0)
print('Part 1:', total)

for grid in data:
    grid = np.array([[*line] for line in grid.splitlines()])

    t2 = checkGrid(grid, False, 1)
    if t2:
        total2 += t2
        continue
    total2 += checkGrid(grid.T, True, 1)
print('Part 2:', total2)