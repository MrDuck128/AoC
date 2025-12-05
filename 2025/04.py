with open('04.txt') as f:
    data = [[1 if x == '@' else 0 for x in row] for row in f.read().splitlines()]

dirs =[(-1,0), (-1, 1), (0, 1), (1, 1), (1,0), (1, -1), (0, -1), (-1, -1)]

totalRolls = 0

while True:
    rolls =[]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if not data[i][j]: continue
            count = 0

            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= len(data) or nj < 0 or nj >= len(data[0]): continue
                if data[ni][nj]: count += 1

            if count < 4:
                rolls.append((i, j))

    if not len(rolls):
        print('Part 2:', totalRolls)
        break

    if totalRolls == 0:
        print('Part 1:', len(rolls))

    totalRolls += len(rolls)

    for (i, j) in rolls:
        data[i][j] = 0