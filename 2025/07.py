from functools import cache

with open('07.txt') as f:
    grid = [list(row) for row in f.read().splitlines()]

seen = set()
maxI = len(grid)
count = 0

@cache
def solve(i, j):
    global count

    if i+1 == maxI: return 1
    elif grid[i+1][j] == '.': return solve(i+1, j)
    elif grid[i+1][j] == '^':
        count += 1
        return solve(i+1, j-1) + solve(i+1, j+1)

count2 = solve(0, grid[0].index('S'))
print('Part 1:', count)
print('Part 2:', count2)