from collections import deque

with open('01.txt') as f:
    data = f.read().splitlines()

d = deque(range(100))
d.rotate(50)

count1, count2 = 0, 0

for ins in data:
    div, amount = divmod(int(ins[1:]), 100)
    count2 += div
    for i in range(amount):
        d.rotate(-1) if ins[0] == 'L' else d.rotate(1)
        if d[0] == 0: count2 += 1
    if d[0] == 0: count1 += 1

print('Part 1:', count1)
print('Part 2:', count2)