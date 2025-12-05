import re

with open('02.txt') as f:
    data = [tuple(map(int, pair.split('-'))) for pair in f.read().split(',')]

total1, total2 = 0, 0
for a, b in data:
    for i in range(a, b+1):
        i = str(i)
        if i[:len(i)//2] == i[len(i)//2:]: total1 += int(i)
        if re.fullmatch(r'^(.+)\1+$',i): total2 += int(i)

print('Part 1:', total1)
print('Part 2:', total2)