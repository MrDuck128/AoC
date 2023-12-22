with open('22.txt') as f:
    bricks = sorted([list(map(int, line.replace('~', ',').split(','))) for line in f.read().splitlines()], key=lambda x: x[2])

def touch(a, b):
    return min(a[3], b[3]) >= max(a[0], b[0]) and min(a[4], b[4]) >= max(a[1], b[1])

for i, brick in enumerate(bricks):
    mz = 0
    for fallen in bricks[:i]:
        if touch(brick, fallen):
            mz = max(mz, fallen[5])

    brick[5] += mz+1 - brick[2]
    brick[2] = mz+1

bricks = sorted(bricks, key=lambda x: x[2])

touchingBelow = {i: set() for i in range(len(bricks))}
touchingAbove = {i: set() for i in range(len(bricks))}

for i, above in enumerate(bricks):
    for j, below in enumerate(bricks[:i]):
        if touch(above, below) and below[5]+1 == above[2]:
            touchingBelow[i].add(j)
            touchingAbove[j].add(i)
            
minus = set()
for v in touchingBelow.values():
    if len(v) == 1:
        minus.add(list(v)[0])

print('Part 1:', len(touchingBelow) - len(minus))

total2 = 0
for brick in minus:
    Q = [brick]
    fall = {brick}

    while Q:
        elem = Q.pop(0)
        for i in touchingAbove[elem]:
            if i not in fall:
                if touchingBelow[i].issubset(fall):
                    Q.append(i)
                    fall.add(i)

    total2 += len(fall) - 1

print('Part 2:', total2)