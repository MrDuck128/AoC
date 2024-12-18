import re

with open('17.txt') as f:
    a, b, c, *program = map(int, re.findall('\d+', f.read()))

def run(a, b, c):
    i, R = 0, []

    while i < len(program):
        vals = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
        op = program[i+1]

        match program[i]:
            case 0: a >>= vals[op]
            case 1: b  ^= op
            case 2: b   = vals[op] % 8
            case 3: i   = op-2 if a else i
            case 4: b  ^= c
            case 5: R  += [vals[op] % 8]
            case 6: b   = a >> vals[op]
            case 7: c   = a >> vals[op]
        i += 2

    return R

print('Part 1:', ','.join(map(str, run(a, b, c))))

Q = [(1, 0)]
for i, a in Q:
    for a in range(a, a+8):
        if run(a, 0, 0) == program[-i:]:
            Q += [(i+1, a*8)]
            if i == len(program):
                print('Part 2:', a)
                break
    else:
        continue
    break