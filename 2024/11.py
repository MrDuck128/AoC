from functools import cache

with open('11.txt') as f:
    stones = [int(x) for x in f.read().split()]

@cache
def calcStones(stone, steps):
    if steps == 0:
        return 1
    
    if stone == 0:
        return calcStones(1, steps-1)
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        half = len(stone) // 2
        return calcStones(int(stone[:half]), steps-1) + calcStones(int(stone[half:]), steps-1)
    else:
        return calcStones(stone*2024, steps-1)

print('Part 1:', sum(calcStones(stone, 25) for stone in stones))
print('Part 2:', sum(calcStones(stone, 75) for stone in stones))