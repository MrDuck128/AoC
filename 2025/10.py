import re
from heapq import heappush, heappop
from z3 import Int, Optimize, Sum, sat

with open('10.txt') as f:
    data = f.read().splitlines()
    diagrams = [tuple([0 if x == '.' else 1 for x in re.findall('\[[.#]+\]', line)[0][1:-1]]) for line in data]
    schematics = [[list(map(int, x.split(','))) for x in re.findall('\(([\d,]+)\)', line)] for line in data]
    joltages = [[list(map(int, x.split(','))) for x in re.findall('\{([\d,]+)\}', line)][0] for line in data]

def solve1(diagram, schematic):
    Q = [(0, tuple(0 for _ in range(len(diagram))))]
    seen = set()

    while Q:
        score, state = heappop(Q)

        if (score, state) in seen: continue
        seen.add((score, state))
        if state == diagram: return score

        for button in schematic:
            heappush(Q, (score+1, tuple([1-v if i in button else v for i, v in enumerate(state)])))

print('Part 1:', sum(solve1(diagram, schematic) for diagram, schematic in zip(diagrams, schematics)))

def solve2(schematic, joltage):
    presses = [Int(f"p{i}") for i in range(len(schematic))]

    s = Optimize()

    for p in presses:
        s.add(p >= 0, p <= max(joltage))

    for i in range(len(joltage)):
        affecting = [presses[enum] for enum, btn in enumerate(schematic) if i in btn]
        s.add(Sum(affecting) == joltage[i])

    s.minimize(Sum(presses))

    if s.check() == sat: return sum([s.model()[p].as_long() for p in presses])

print('Part 2:', sum(solve2(schematic, joltage) for schematic, joltage in zip(schematics, joltages)))