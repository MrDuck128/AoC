with open('25.txt') as f:
    schematics = [[list(line) for line in schematic.splitlines()] for schematic in f.read().split('\n\n')]

locks = [schematic for schematic in schematics if all(x == '#' for x in schematic[0])]
keys = [schematic for schematic in schematics if all(x == '#' for x in schematic[-1])]

w, h = len(locks[0][0]), len(locks[0])

locksT = [list(map(list, zip(*lock))) for lock in locks]
keysT = [list(map(list, zip(*key))) for key in keys]

total = 0
for lock in locksT:
    lockHeights = [lline.count('#') for lline in lock]
    
    for key in keysT:
        keyHeights = [kline.count('#') for kline in key]

        if all(lockHeights[i] + keyHeights[i] <= h for i in range(w)):
            total += 1

print('Part 1:', total)