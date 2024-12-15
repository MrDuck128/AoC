with open('15.txt') as f:
    grid, instructions = f.read().split('\n\n')

grid = [list(line) for line in grid.splitlines()]
instructions = instructions.replace('\n', '')

dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

gridExpansion = {'#': '##', 'O': '[]', '.': '..', '@': '@.', }
extendedGrid = [list(''.join(gridExpansion[c] for c in line)) for line in grid]

def solve(grid, instructions, ri, rj, part1=False):
    for inst in instructions:
        boxes = [(ri, rj, '@')]
        di, dj = dirs[inst]
        canMove = True

        for (i, j, _) in boxes:
            ni, nj = i+di, j+dj
            if (ni, nj, '[') in boxes or (ni, nj, ']') in boxes: continue
            newPos = grid[ni][nj]
            if newPos == '#': 
                canMove = False
                break
            elif newPos == 'O': boxes.append((ni, nj, 'O'))
            elif newPos == '[':
                boxes.append((ni, nj, '['))
                boxes.append((ni, nj+1, ']'))
            elif newPos == ']':
                boxes.append((ni, nj, ']'))
                boxes.append((ni, nj-1, '['))

        if canMove:
            for (bi, bj, el) in boxes[1:]:
                grid[bi][bj] = '.'
            for (bi, bj, el) in boxes[1:]:
                grid[bi+di][bj+dj] = el

            grid[ri][rj] = '.'
            ri, rj = ri+di, rj+dj
            grid[ri][rj] = '@'

    boxSymbol = 'O' if part1 else '['
    return sum(i*100+j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == boxSymbol)

ri, rj = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '@'][0]
print('Part 1:', solve(grid, instructions, ri, rj, True))

ri, rj = [(i, j) for i in range(len(extendedGrid)) for j in range(len(extendedGrid[0])) if extendedGrid[i][j] == '@'][0]
print('Part 2:', solve(extendedGrid, instructions, ri, rj))