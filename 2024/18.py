from collections import deque

with open('18.txt') as f:
    coords = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

size = 71
memory = 1024

def bfs(memory):
    Q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    corrupted = set(coords[:memory])

    while Q:
        i, j, d = Q.popleft()

        for ni, nj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if not(-1 < ni < size and -1 < nj < size): continue
            if (ni, nj) in seen: continue
            if (ni, nj) in corrupted: continue
            if ni == nj == size-1: return d+1

            Q.append((ni, nj, d+1))
            seen.add((ni, nj))

    return 0

print('Part 1:', bfs(memory))

l = 0
h = len(coords)-1
while l < h-1:
    m = (h+l) // 2
    if bfs(m):
        l = m
    else:
        h = m

print('Part 2:', ','.join(str(x) for x in coords[m]))