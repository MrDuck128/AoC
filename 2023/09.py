with open('09.txt') as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

def getHistory(line):
    fullHistory = [line]
    k = 0
    while True:
        currLine = fullHistory[k]

        if set(currLine) == {0}:
            history = 0
            for line in fullHistory:
                history += line[-1]
            return history
        
        fullHistory.append([b - a for a, b in zip(currLine, currLine[1:])])
        k += 1

total = 0
for line in data:
    total += getHistory(line)
print('Part 1:', total)

total = 0
for line in data:
    total += getHistory(line[::-1])
print('Part 2:', total)