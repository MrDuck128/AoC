from heapq import heappop, heappush

with open('17.txt') as f:
	grid = [list(map(int, line)) for line in f.read().splitlines()]

# cost, i, j, di, dj, step
Q = [(0, 0, 0, 0, 1, 0)]
seen = set()
while Q:
	cost, i, j, di, dj, step = heappop(Q)

	if (i, j) == (len(grid)-1, len(grid[0])-1):
		print('Part 1:', cost)
		break

	if (i, j, di, dj, step) in seen: continue
	seen.add((i, j, di, dj, step))

	if step < 3 and (di, dj) != (0, 0):
		if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]): 
			heappush(Q, (cost+grid[i+di][j+dj], i+di, j+dj, di, dj, step+1))

	for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		if (di, dj) not in [(ii, jj), (-ii, -jj)]:
			if 0 <= i+ii < len(grid) and 0 <= j+jj < len(grid[0]): 
				heappush(Q, (cost+grid[i+ii][j+jj], i+ii, j+jj, ii, jj, 1))

Q = [(0, 0, 0, 0, 1, 0)]
seen = set()
while Q:
	cost, i, j, di, dj, step = heappop(Q)

	if (i, j) == (len(grid)-1, len(grid[0])-1) and step >= 4:
		print('Part 2:', cost)
		break

	if (i, j, di, dj, step) in seen: continue
	seen.add((i, j, di, dj, step))

	if step < 10 and (di, dj) != (0, 0):
		if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]): 
			heappush(Q, (cost+grid[i+di][j+dj], i+di, j+dj, di, dj, step+1))

	if step >= 4 or (i, j) == (0, 0):
		for ii, jj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			if (di, dj) not in [(ii, jj), (-ii, -jj)]:
				if 0 <= i+ii < len(grid) and 0 <= j+jj < len(grid[0]): 
					heappush(Q, (cost+grid[i+ii][j+jj], i+ii, j+jj, ii, jj, 1))