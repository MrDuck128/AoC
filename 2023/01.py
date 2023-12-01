import re

with open('01.txt') as f:
    data = f.read().splitlines()

numbers = []

for line in data:
    digitList = [str(d) for d in line if d.isdigit()]
    numbers.append(int(digitList[0] + digitList[-1]))

print('Part 1:', sum(numbers))


numbers2 = []

r = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in data:
    for digit, num in r.items():
        if digit in line:
            indices = [index.start() for index in re.finditer(digit, line)]
            for index in reversed(indices):
                line = line[:index+1] + str(num) + line[index+1:]

    digitList = [str(d) for d in line if d.isdigit()]
    numbers2.append(int(digitList[0] + digitList[-1]))

print('Part 2:', sum(numbers2))