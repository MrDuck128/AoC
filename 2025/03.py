with open('03.txt') as f:
    banks = f.read().splitlines()

def largestNum(bank, nDigs, start=0):
    number = ''
    for i in range(nDigs-1, -1, -1):
        range_ = bank[start:-i] if i != 0 else bank[start:]
        bigDig = max(range_)
        number += str(bigDig)
        start += range_.find(bigDig) + 1
    return int(number)

total1, total2 = 0, 0

for bank in banks:
    total1 += largestNum(bank, 2)
    total2 += largestNum(bank, 12)

print('Part 1:', total1)
print('Part 2:', total2)