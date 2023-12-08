from collections import deque
from math import gcd

with open('08.txt') as f:
    data = f.read().split('\n\n')

def lcm(a,b):
    return a*b//gcd(a,b)

inst = deque(data[0])
m = {a: (l, r) for a, l, r in [line.replace('(', '').replace(')', '').replace(',', '').replace('=', '').split() for line in data[1].splitlines()]}

currNode = 'AAA'
counter = 0
while True:
    if currNode == 'ZZZ':
        break
    if inst[0] == 'L':
        currNode = m[currNode][0]
    else:
        currNode = m[currNode][1]
    inst.rotate(-1)
    counter += 1

print('Part 1:', counter)

currNodes = [node for node in m if node[-1] == 'A']
finishedNodes = []
counter = 0
while currNodes:
    for i in range(len(currNodes)):
        if inst[0] == 'L':
            currNodes[i] = m[currNodes[i]][0]
        else:
            currNodes[i] = m[currNodes[i]][1]
    inst.rotate(-1)
    counter += 1
    
    for i in range(len(currNodes)-1, -1, -1):
        if currNodes[i][-1] == 'Z':
            currNodes.pop(i)
            finishedNodes.append(counter)

currMultiple = 1
for i in range(len(finishedNodes)):
    currMultiple = lcm(currMultiple, finishedNodes[i])

print('Part 2:', currMultiple)