from collections import defaultdict

with open('22.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

def mixAndPrune(num, x):
    return num^x % 16777216

def secretNum(num):
    num = mixAndPrune(num, num * 64)
    num = mixAndPrune(num, num // 32)
    num = mixAndPrune(num, num * 2048)
    return num

lastNumTotal = 0
lastDigList = []
for num in numbers:
    lastDigs = [num % 10]
    for i in range(2000):
        num = secretNum(num)
        lastDigs.append(num % 10)
    lastNumTotal += num
    lastDigList.append(lastDigs)
print('Part 1:', lastNumTotal)

diffsList = [[b-a for a, b in zip(lastDigs, lastDigs[1:])] for lastDigs in lastDigList]

allSeqs = defaultdict(int)
for i, diffs in enumerate(diffsList):
    bananas = set()
    for j, (a, b, c, d) in enumerate(zip(diffs, diffs[1:], diffs[2:], diffs[3:])):
        if (a, b, c, d) in bananas: continue
        bananas.add((a, b, c, d))
        allSeqs[(a, b, c, d)] += lastDigList[i][j+4]
print('Part 2:', max(allSeqs.values()))