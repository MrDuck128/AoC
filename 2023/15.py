from functools import reduce

with open('15.txt') as f:
    data = f.read().strip().split(',')

hash = lambda seq: reduce(lambda value, char: ((value + ord(char)) * 17) % 256, seq, 0)

print('Part 1:', sum(map(hash, data)))

boxes = [{} for _ in range(256)]

for seq in data:
    match seq.strip('-').split('='):
        case [lens, focal]: boxes[hash(lens)][lens] = int(focal)
        case [lens]: boxes[hash(lens)].pop(lens, 0)

print('Part 2:', sum(b * slot * focal for b, box in enumerate(boxes, 1) for slot, focal in enumerate(box.values(), 1)))