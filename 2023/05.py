with open('05.txt') as f:
    data = f.read().split('\n\n')

def getLocation(seed):
    for map in mapList:
        for x1, x2, y in map:
            if x1 <= seed <= x2:
                seed = y + seed - x1
                break
    return seed

def getNextSeed(range, map):
    i, ranges = 0, []
    while True:
        conv = map[i]
        if range[0] < conv[0]:
            if range[1] < conv[0]:
                ranges.append(range)
                return ranges
            ranges.append((range[0], conv[0]-1))
            range = (conv[0], range[1])
        elif conv[0] <= range[0] <= conv[1]:
            diff = conv[2] - conv[0]
            if range[1] <= conv[1]:
                ranges.append((range[0]+diff, range[1]+diff))
                return ranges
            ranges.append((range[0]+diff, conv[1]+diff))
            range = (conv[1]+1, range[1])
        elif conv[1] < range[0]:
            i += 1
            if i == len(map):
                ranges.append(range)
                return ranges

seeds = [int(seed) for seed in data[0].split()[1:]]

mapList = []
for map in data[1:]:
    mapRanges = []
    for section in map.splitlines()[1:]:
        y, x, r = [int(num) for num in section.split()]
        mapRanges.append((x, x+r-1, y))
    mapList.append(mapRanges)

locationList = [] 
for seed in seeds:
    locationList.append(getLocation(seed))
print('Part 1:', min(locationList))

seeds2 = [(seeds[r], seeds[r] + seeds[r+1]-1) for r in range(0, len(seeds), 2)]

for map in mapList:
    seeds2 = sum((getNextSeed(range, sorted(map)) for range in seeds2), [])
print('Part 2:', sorted(seeds2)[0][0])