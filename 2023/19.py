import re
from math import prod

with open('19.txt') as f:
    workflowsTemp, partsTemp = f.read().split('\n\n')

workflows = {}
for wf in workflowsTemp.splitlines():
    name, rulesTemp = wf[:-1].split('{')
    rules = [rule.split(':') for rule in rulesTemp.split(',')]
    workflows[name] = rules
parts = [tuple(int(x) for x in re.findall(r'\d+', part)) for part in partsTemp.splitlines()]

def testAccepted(x, m, a, s, wf):
    while True:
        for rule in workflows[wf]:
            if len(rule) == 1:
                wf = rule[0]
                break
            if eval(rule[0]):
                wf = rule[1]
                break
        if wf == 'A': return True
        elif wf == 'R': return False

print('Part 1:', sum([sum([x, m, a, s]) for (x, m, a, s) in parts if testAccepted(x, m, a, s, 'in')]))

p = []
Q = [('in', {l: (1, 4000) for l in 'xmas'})]
while Q:
    wf, ranges = Q.pop(0)

    if wf == 'A':
        p.append(prod([b-a+1 for (a, b) in ranges.values()]))
        continue
    elif wf == 'R':
        continue

    for rule in workflows[wf]:
        match re.split('([<>])', rule[0]):
            case [dwf]:
                Q.append((dwf, ranges.copy()))
            case [l, '>', val]:
                a, b = ranges[l]
                val = int(val)
                ranges[l] = (max(a, val+1), b)
                Q.append((rule[1], ranges.copy()))
                ranges[l] = (a, min(b, val))
            case [l, '<', val]:
                a, b = ranges[l]
                val = int(val)
                ranges[l] = (a, min(b, val-1))
                Q.append((rule[1], ranges.copy()))
                ranges[l] = (max(a, val), b)

print('Part 2:', sum(p))