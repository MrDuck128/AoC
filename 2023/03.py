from collections import defaultdict

with open('03.txt') as f:
    data = f.read().splitlines()

def checkPartNumber(currentPartIndices):

    leftI, leftJ = currentPartIndices[0]
    rightI, rightJ = currentPartIndices[-1]

    if leftI != 0: leftI -= 1
    if leftJ != 0: leftJ -= 1
    if rightI != gridRows-1: rightI += 1
    if rightJ != gridColumns-1: rightJ += 1

    for i in range(leftI, rightI+1):
        for j in range(leftJ, rightJ+1):
            if data[i][j] not in '0123456789.':
                if data[i][j] == '*':
                    gears[(i, j)].append(int(''.join(str(data[i][j]) for (i, j) in currentPartIndices)))
                return True
    return False

def addPartNumber(currentPartIndices):
    a = [str(data[i][j]) for (i, j) in currentPartIndices]
    number = int(''.join(a))
    partNumbers.append(number)

newPartNumber = True
currentPartIndices = []
partNumbers = []
gears = defaultdict(list)

gridRows = len(data)
gridColumns = len(data[0])
for i in range(gridRows):
    for j in range(gridColumns):
        if data[i][j].isnumeric():
            if newPartNumber:
                currentPartIndices = []
                newPartNumber = False

            currentPartIndices.append((i, j))
            if j == gridColumns-1 or not data[i][j+1].isnumeric():
                newPartNumber = True
                if checkPartNumber(currentPartIndices):
                    addPartNumber(currentPartIndices)

print('Part 1:', sum(partNumbers))

gearRatios = []
for _, gearList in gears.items():
    if len(gearList) == 2:
        gearRatios.append(gearList[0] * gearList[1])
print('Part 2:', sum(gearRatios))