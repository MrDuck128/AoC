with open('01.txt') as f:
    data = f.read().splitlines()

A = [int(line.split()[0]) for line in data]
B = [int(line.split()[1]) for line in data]

print('Part 1:', sum(abs(a-b) for a, b in zip(sorted(A), sorted(B))))
print('Part 2:', sum(x * B.count(x) for x in A))