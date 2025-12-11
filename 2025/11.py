from collections import defaultdict
from functools import cache

with open('11.txt') as f:  
    G = defaultdict(list, {k: dsts.split() for line in f.read().splitlines() for k, dsts in [line.split(': ')]})

@cache
def count(src, dst):
    return (src == dst) + sum(count(s, dst) for s in G[src])
    
print('Part 1:', count('you', 'out'))
print('Part 2:', count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out') +
                 count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out'))