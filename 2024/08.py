from collections import defaultdict
d = defaultdict(list)

with open('08.txt') as f:
    data = [list(line) for line in f.read().splitlines()]

maxI, maxJ = len(data), len(data[0])

for i, line in enumerate(data):
    for j, el in enumerate(list(line)):
        if el != '.':
            d[el].append((i, j))

antinodes = set()
antinodes2 = set()
for coords in d.values():
    combos = [(a, b) for i, a in enumerate(coords) for b in coords[i+1:]]
    
    for (ar, ac), (br, bc) in combos:
        dr = br - ar
        dc = bc - ac

        firstLeft = firstRight = True
        ar, ac = ar-dr, ac-dc
        br, bc = br+dr, bc+dc

        while -1 < ar < maxI and -1 < ac < maxJ:
            if firstLeft:
                antinodes.add((ar, ac))
                firstLeft = False
            antinodes2.add((ar, ac))
            ar, ac = ar-dr, ac-dc
            
        while -1 < br < maxI and -1 < bc < maxJ:
            if firstRight:
                antinodes.add((br, bc))
                firstRight = False
            antinodes2.add((br, bc))
            br, bc = br+dr, bc+dc

print('Part 1:', len(antinodes))

antennas = sum(1 for vals in d.values() if len(vals) > 1 for val in vals if val not in antinodes2)
print('Part 2:', antennas + len(antinodes2))