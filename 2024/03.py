import re

with open('03.txt') as f:
    data = f.read()

strings = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data)

def mul(a, b):
    return a * b

total1 = total2 = 0
enable = True

for string in strings:
    if string == 'do()':
        enable = True
    elif string == "don't()":
        enable = False
    else:
        val = eval(string)
        total1 += val
        total2 += val * enable

print('Part 1:', total1)
print('Part 2:', total2)