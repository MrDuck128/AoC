with open('16.txt') as f:
	grid = [[*line] for line in f.read().splitlines()]

def energize(grid, start):
	beams = [start]
	seen = set()
	while beams:
		i, j, di, dj = beams.pop(0)

		if (i, j, di, dj) in seen: continue
		if not (0 <= i < len(grid) and 0 <= j < len(grid)): continue
		seen.add((i, j, di, dj))
		
		match grid[i][j]:
			case '|':
				if dj:
					di, dj = -1, 0
					beams.append((i+1, j, 1, 0))
			case '-':
				if di:
					di, dj = 0, -1
					beams.append((i, j+1, 0, 1))
			case '/':
				di, dj = -dj, -di
			case '\\':
				di, dj = dj, di
		
		beams.append((i+di, j+dj, di, dj))

	return(len({(i, j) for (i, j, _, _) in seen}))

print('Part 1:', energize(grid, (0, 0, 0, 1)))

energizeVars = []
for i in range(len(grid)):
	energizeVars.append(energize(grid, (i, 0, 0, 1)))
	energizeVars.append(energize(grid, (i, len(grid)-1, 0, -1)))
for j in range(len(grid)):
	energizeVars.append(energize(grid, (0, j, 1, 0)))
	energizeVars.append(energize(grid, (len(grid)-1, j, -1, 0)))
print('Part 2:', max(energizeVars))