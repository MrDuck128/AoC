with open('10.txt') as f:
    grid = [[*line] for line in f.read().splitlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pipes = []
pTypes = ['|', '-', 'L', 'J', 'J', '7', 'F']

sI, sJ = [(i, grid.index('S')) for i, grid in enumerate(grid) if 'S' in grid][0]

for d, (i, j) in enumerate(dirs):
    if grid[sI+i][sJ+j] in pTypes:
        pipes.append((sI+i, sJ+j, d))

maxI = len(grid)-1
maxJ = len(grid[0])-1

# 0 NORTH, 1 EAST, 2 SOUTH, 3 WEST
def continuePipe(i, j, d):
    match grid[i][j]:
        case '.':
            return -1, 0, 0
        case '|':
            if d == 0 and i != 0: return i-1, j, d
            elif d == 2 and i != maxI: return i+1, j, d
            else: return -1, 0, 0
        case '-':
            if d == 1 and j != maxJ: return i, j+1, d
            elif d == 3 and j != 0: return i, j-1, d
            else: return -1, 0, 0
        case 'L':
            if d == 2 and j != maxJ: return i, j+1, 1
            elif d == 3 and i != 0: return i-1, j, 0
            else: return -1, 0, 0
        case 'J':
            if d == 2 and j != 0: return i, j-1, 3
            elif d == 1 and i != 0: return i-1, j, 0
            else: return -1, 0, 0

        case '7':
            if d == 0 and j != 0: return i, j-1, 3
            elif d == 1 and i != maxI: return i+1, j, 2
            else: return -1, 0, 0

        case 'F':
            if d == 0 and j != maxJ: return i, j+1, 1
            elif d == 3 and i != maxI: return i+1, j, 2
            else: return -1, 0, 0

pipeCoords = set()
pipeCoords.add((sI, sJ))
while pipes:
    i, j, d = pipes.pop(0)
    counter = 1
    while True:
        pipeCoords.add((i, j))
        i, j, d = continuePipe(i, j, d)
        if i == -1:
            counter = 0
            break
        counter += 1
        if grid[i][j] == 'S':
            break
    if counter:
        print('Part 1:', counter // 2)
        break

# Change irrelevant pipes to blank spaces
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '.' and (i, j) not in pipeCoords:
            grid[i][j] = '.'

# Insert spaces between each row and column
jRng = (len(grid[0])-1) * 2
for i in range(len(grid)):
    for j in range(0, jRng, 2):
        if grid[i][j] in ('S', 'F', '-', 'L') and grid[i][j+1] in ('J', '-', '7', 'S'):
            grid[i].insert(j+1, '-')
        else:
            grid[i].insert(j+1, '*')

for i in range(0, maxI*2, 2):
    grid.insert(i+1, ['x' for _ in range(len(grid[0]))])

for i in range(0, len(grid)-1, 2):
    for j in range(len(grid[0])):
        if grid[i][j] in ('S', 'F', '|', '7') and grid[i+2][j] in ('J', '|', 'L', 'S'):
            grid[i+1][j] = '|'
        else:
            grid[i+1][j] = '*'

# Change outside blank spaces to outside
for j in range(len(grid[0])):
    if grid[0][j] in ('.', '*'):
        grid[0][j] = 'O'
    if grid[-1][j] in ('.', '*'):
        grid[-1][j] = 'O'

for i in range(len(grid)):
    if grid[i][0] in ('.', '*'):
        grid[i][0] = 'O'
    if grid[i][-1] in ('.', '*'):
        grid[i][-1] = 'O'

# Fill from outside inward
for _ in range(70):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in ('.', '*'):
                for dI, dJ in dirs:
                    if grid[i+dI][j+dJ] == 'O':
                        grid[i][j] = 'O'
                        break

spaces = 0
for line in grid:
    for symbol in line:
        if symbol == '.':
            spaces += 1
print('Part 2:', spaces)