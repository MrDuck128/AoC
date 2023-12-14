import numpy as np

with open('14.txt') as f:
    startGrid = grid = np.array([[*line] for line in f.read().splitlines()])

# 0 EAST, 1 SOUTH, 2 WEST, 3 NORTH
def tilt(grid, dir = 0):
    for _ in range(dir):
        grid = np.rot90(grid)

    tiltedGrid = []
    for line in grid:
        segments = []
        line = ''.join(line).split('#')

        for segment in line:
            if 'O' not in segment:
                segments.append(segment)
                continue

            numDot = segment.count('.')
            segment = segment.replace('.', '')

            segments.append('.'*numDot + segment)

        line = [x for x in '#'.join(segments)]
        tiltedGrid.append(line)
    
    tiltedGrid = np.array(tiltedGrid)
    for _ in range(dir):
        tiltedGrid = np.rot90(tiltedGrid, axes=(1, 0))

    return tiltedGrid
    
def calcLoad(grid):
    for _ in range(2):
        grid = np.rot90(np.array(grid))
    
    total = 0
    for i, line in enumerate(grid):
        total += (i+1) * np.count_nonzero(line == 'O')
    return total

print('Part 1:', calcLoad(tilt(grid, 3)))

seen = {}
cycleDiff = 0
cycleStart = 0
for cycle in range(1, 1000000001):
    gridHash = ''.join([''.join([*line]) for line in grid])
    if gridHash in seen:
        cycleStart = seen[gridHash]
        cycleDiff = cycle - seen[gridHash]
        break

    for i in range(4):
        grid = tilt(grid, 3-i)

    seen[gridHash] = cycle

# (1000000000-cycleStart) % cycleDiff + cycleStart
for cycle in range((1000000000-cycleStart) % cycleDiff + 1):
    for i in range(4):
        grid = tilt(grid, 3-i)
print('Part 2:', calcLoad(grid))