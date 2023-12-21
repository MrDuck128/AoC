from math import gcd

with open('20.txt') as f:
    data = f.read().splitlines()

def lcm(a,b):
    return a*b//gcd(a,b)

flipflop = {}
conjunction = {}
for line in data:
    src, dst = line.split(' -> ')
    dst = (dst.split(', '))
    match src[0]:
        case 'b': broadcaster = dst
        case '%': flipflop[src[1:]] = [0, dst]
        case '&': conjunction[src[1:]] = [{}, dst]
for line in data:
    src, dst = line.split(' -> ')
    dst = (dst.split(', '))
    for d in dst:
        if d in conjunction:
            conjunction[d][0][src[1:]] = 'low'

impVals = [k for val in conjunction.values() for k in val[0] if val[1] == ['rx']]
impValDiff = {key: 0 for key in impVals}
[finSrc] = [key for key, value in conjunction.items() if 'rx' in value[1]]
highCount = lowCount = buttonPress = 0
while True:
    buttonPress += 1
    Q = [('button', 'low', 'broadcaster')]

    while Q:
        src, pulse, dst = Q.pop(0)

        if src in impValDiff and pulse == 'high' and dst == finSrc:
            if impValDiff[src] == 0:
                impValDiff[src] = buttonPress

        if buttonPress == 15_000:
            LCM = 1
            for val in impValDiff.values():
                LCM = lcm(LCM, val)
            print('Part 2:', LCM)
            exit(0)
        
        if pulse == 'high': highCount += 1
        else: lowCount += 1

        if dst == 'broadcaster':
            for ndst in broadcaster:
                Q.append((dst, 'low', ndst))
        elif dst in flipflop:
            if pulse == 'low':
                flipflop[dst][0] = 0 if flipflop[dst][0] else 1
                for ndst in flipflop[dst][1]:
                    Q.append((dst, 'high' if flipflop[dst][0] else 'low', ndst))
        elif dst in conjunction:
            conjunction[dst][0][src] = pulse
            if all(val in 'high' for val in conjunction[dst][0].values()):
                for ndst in conjunction[dst][1]:
                    Q.append((dst, 'low', ndst))
            else:
                for ndst in conjunction[dst][1]:
                    Q.append((dst, 'high', ndst))

    if buttonPress == 1000:
        print('Part 1:', highCount * lowCount)