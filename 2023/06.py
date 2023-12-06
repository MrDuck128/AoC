with open('06.txt') as f:
    data = f.read().splitlines()

times = [int(x) for x in data[0].split()[1:]]
distances = [int(x) for x in data[1].split()[1:]]

def solve(time, distance):
    for i in range(1, time//2+1):
        if (time-i) * i > distance:
            start = i
            break
    return time - start*2 + 1

ways = 1
for time, distance in zip(times, distances):
    ways *= solve(time, distance)
print('Part 1:', ways)

time = int(''.join(str(x) for x in times))
distance = int(''.join(str(x) for x in distances))
print('Part 2:', solve(time, distance))