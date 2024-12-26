from collections import deque
from itertools import product
from functools import cache

with open('21.txt') as f:
    codes = f.read().splitlines()

numpadVals = ['789', '456', '123', 'N0A']
keypadVals = ['N^A', '<v>']

def getSeqs(padVals):
    maxI, maxJ = len(padVals), len(padVals[0])
    indices = {padVals[i][j]: (i, j) for i in range(maxI) for j in range(maxJ) if padVals[i][j] != 'N'}

    seqs = {}
    for a in indices:
        for b in indices:
            if a == b:
                seqs[(a, b)] = ['A']
                continue

            optimalLen = float('inf')
            Q = deque([(indices[a], '')])
            paths = []
            while Q:
                (i, j), path = Q.popleft()

                for ni, nj, npath in [(i-1, j, '^'), (i, j+1, '>'), (i+1, j, 'v'), (i, j-1, '<')]:
                    if not(-1 < ni < maxI and -1 < nj < maxJ): continue
                    if padVals[ni][nj] == 'N': continue
                    
                    if padVals[ni][nj] == b:
                        if optimalLen < len(path) + 1: break # stop if path not optimal
                        optimalLen = len(path) + 1 
                        paths.append(path + npath + 'A')
                    else:
                        Q.append(((ni, nj), path + npath))
                else:
                    continue
                break

            seqs[(a, b)] = paths
    return seqs
                    
numpadSeqs = getSeqs(numpadVals)
keypadSeqs = getSeqs(keypadVals)
keypadLengths = {k: len(v[0]) for k, v in keypadSeqs.items()}

@cache
def getLength(seq, depth=25):
    if depth == 1:
        return sum(keypadLengths[(a, b)] for a, b in zip('A' + seq, seq))
    length = 0
    for a, b in zip('A' + seq, seq):
        length += min(getLength(subseq, depth-1) for subseq in keypadSeqs[(a, b)])
    return length

total1 = total2 = 0
for code in codes:
    options = [numpadSeqs[(a, b)] for a, b in zip('A' + code, code)]
    inputs = [''.join(path) for path in product(*options)]

    length1 = min(getLength(input, 2) for input in inputs)
    length2 = min(getLength(input, 25) for input in inputs)
    total1 += length1 * int(code[:-1])
    total2 += length2 * int(code[:-1])
    
print('Part 1:', total1)
print('Part 2:', total2)