with open('09.txt') as f:
    data = f.read()

disk = []
fId = 0
diskMap = {}
blanksRanges = []
index = 0

for i, length in enumerate(data):
    length = int(length)
    if i % 2 == 0:
        disk += [fId] * length
        diskMap[fId] = (index, length)
        fId += 1
    else:
        disk += [-1] * length
        if length != 0:
            blanksRanges.append((index, length))
    index += length

def part1(disk):
    blanks = [i for i, val in enumerate(disk) if val == -1]

    for i in blanks:
        while i < len(disk):
            val = disk.pop()
            if val == -1: continue

            disk[i] = val
            break

    return sum(i * val for i, val in enumerate(disk))

def part2(disk, diskMap, blanksRanges):
    for file, (index, length) in reversed(diskMap.items()):
        for i, (bs, bl) in enumerate(blanksRanges):
            if bs >= index:
                blanksRanges = blanksRanges[:i]
                break
            if bl >= length:
                disk[bs:bs+length] = [file] * length
                disk[index:index+length] = [-1] * length
                if bl == length:
                    del blanksRanges[i]
                else:
                    blanksRanges[i] = (bs+length, bl-length)
                break

    return sum(i * val for i, val in enumerate(disk) if val != -1)

print('Part 1:', part1(disk.copy()))
print('Part 2:', part2(disk, diskMap, blanksRanges))