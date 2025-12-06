from math import prod

with open('06.txt') as f:
    data = f.read().splitlines()
    rows = [[x for x in row.split()] for row in data]
    cols = [list(row) for row in data]

total1 = 0
for row in zip(*rows):
    vals = map(int, row[:-1])
    if row[-1] == '+': total1 += sum(vals)
    else: total1 += prod(vals)

print('Part 1:', total1)

sections, section = [], []
for col in zip(*cols):
    if set(col) == set(' '):
        sections.append(section)
        section = []
        continue
    elif col[-1] != ' ':
        section.append(col[-1])
    section.append(int(''.join(col[:-1])))
sections.append(section)

total2 = 0
for section in sections:
    if section[0] == '+': total2 += sum(section[1:])
    else: total2 += prod(section[1:])

print('Part 2:', total2)