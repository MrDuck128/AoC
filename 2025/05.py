with open('05.txt') as f:
    ranges, ings = f.read().split('\n\n')
    ranges = [tuple(map(int,x.split('-'))) for x in ranges.splitlines()]
    ings = [int(x)for x in ings.splitlines()]

print('Part 1:', sum(any(a <= ing <= b for a, b in ranges) for ing in ings))

total, pb = 0, 0
for a, b in sorted(ranges):
    if b <= pb and a <= pb: continue
    elif a <= pb: total += b - pb
    else:total += b - a + 1
    pb = b

print('Part 2:', total)