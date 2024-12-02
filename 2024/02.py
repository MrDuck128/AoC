with open('02.txt') as f:
    data = [list(map(int, line.split())) for line in f.read().splitlines()]

def safe(line):
    diffs = [b-a for a, b in zip(line, line[1:])]

    return 1 if set(diffs) <= {1, 2, 3} or set(diffs) <= {-1, -2, -3} else 0

print('Part 1:', sum(safe(line) for line in data))
print('Part 2:', sum(any(safe(line[:i]+line[i+1:]) for i in range(len(line))) for line in data))