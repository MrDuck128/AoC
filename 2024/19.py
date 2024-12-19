with open('19.txt') as f:
    patterns, towels = f.read().split('\n\n')

patterns = patterns.split(', ')
towels = towels.splitlines()

cache = {}
def possible(towel):
    if towel in cache: return cache[towel]
    if len(towel) == 0: return 1
    
    val = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            val += possible(towel[len(pattern):])

    cache[towel] = val
    return val

total1 = total2 = 0
for towel in towels:
    val = possible(towel)
    if val: total1 += 1
    total2 += val

print('Part 1:', total1)
print('Part 2:', total2)