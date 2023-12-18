with open('18.txt') as f:
    data = [(line.split()[0], int(line.split()[1]), line.split()[2]) for line in f.read().splitlines()]

m = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
m2 = {3: (-1, 0), 0: (0, 1), 1: (1, 0), 2: (0, -1)}

def calcLava(coords, perim):
    area = 0
    for i in range(len(coords)-1):
        area += coords[i][0]*coords[i+1][1] - coords[i+1][0]*coords[i][1]
    area = abs(area) + perim
    return area // 2 + 1

coords, perim = [(0, 0)], 1
for d, val, col in data:
    perim += val
    di, dj = m[d]
    i, j = coords[-1]
    coords.append((i+di*val, j+dj*val))

print('Part 1:', calcLava(coords, perim))

coords, perim = [(0, 0)], 1
for _, _, col in data:
    d, val = int(col[7]), int(col[2:7], 16)
    perim += val
    di, dj = m2[d]
    i, j = coords[-1]
    coords.append((i+di*val, j+dj*val))

print('Part 2:', calcLava(coords, perim))