import re
import numpy as np

with open('13.txt') as f:
    machines = f.read().split('\n\n')

machines = [[int(x) for x in re.findall('\d+', machine)] for machine in machines]

def solve(ax, ay, bx, by, px, py, inc=0):
    coefMat = np.array([[ax, bx], [ay, by]])
    res = np.array([px, py]) + inc
    solution = np.linalg.solve(coefMat, res)
    a, b = [round(x) for x in solution]

    return a*3+b if (a*ax+b*bx, a*ay+b*by) == (px+inc, py+inc) else 0

print('Part 1:', sum(solve(*machine) for machine in machines))
print('Part 2:', sum(solve(*machine, 10000000000000) for machine in machines))