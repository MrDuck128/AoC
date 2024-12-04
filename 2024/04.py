with open('04.txt') as f:
    data = [list(line) for line in f.read().splitlines()]

maxX, maxY = len(data[0]), len(data)
letterSequence = 'MAS'

def checkDirs(x, y):
    count = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for i, letter in enumerate(letterSequence, start=1):
            nx, ny = x+dx*i, y+dy*i

            if 0 <= nx < maxX and 0 <= ny < maxY:
                if letterSequence[i-1] != data[ny][nx]:
                    break

                elif letter == 'S':
                    count += 1

    return count

def checkDirsA(x, y):
    count = 0
    around = []
    for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < maxX and 0 <= ny < maxY:
            if data[ny][nx] not in ('M', 'S'):
                break

            around.append(data[ny][nx])

    if around.count('M') == 2 and around.count('S') == 2 and around[0] != around[2]:
        count += 1

    return count

total1 = total2 = 0
for y in range(maxY):
    for x in range(maxX):
        if data[y][x] == 'X':
            total1 += checkDirs(x, y)
        if 0 < x < maxX and 0 < y < maxY and data[y][x] == 'A':
            total2 += checkDirsA(x, y)

print('Part 1:', total1)
print('Part 2:', total2)