from itertools import product

with open('07.txt') as f:
    data = {int(value): numbers.split() for line in f.read().splitlines() for value, numbers in [line.split(': ')]}

def solve(operations):
    total = 0
    for value, numbers in data.items():
        for combo in product(operations, repeat=len(numbers)-1):
            eqVal = int(numbers[0])
            for op, num in zip(combo, numbers[1:]):
                if op == '+':
                    eqVal += int(num)
                elif op == '*':
                    eqVal *= int(num)
                elif op == '||':
                    eqVal = int(str(eqVal) + num)
            
            if value == eqVal:
                total += value
                break
    return total

print('Part 1:', solve(['+', '*']))
print('Part 2:', solve(['+', '*', '||']))