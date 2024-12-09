from collections import defaultdict
import networkx as nx

with open('05.txt') as f:
    rulesRaw, updatesRaw = f.read().split('\n\n')

rules = defaultdict(list)
updates = []

for rule in rulesRaw.splitlines():
    a, b = rule.split('|')
    rules[b].append(a)

for update in updatesRaw.splitlines():
    updates.append(update.split(','))

def ordered(update):
    for i in range(len(update)):
        if any(x in rules[update[i]] for x in update[i+1:]):
            return False
    return True

def stableTopologicalSort(rules, items):
    G = nx.DiGraph()
    
    for key, dependencies in rules.items():
        for dep in dependencies:
            G.add_edge(dep, key)

    G = G.subgraph(update)

    topogSorted = list(nx.topological_sort(G))
    return topogSorted

total1 = total2 = 0
for update in updates:
    if ordered(update):
        total1 += int(update[len(update)//2])
    else:
        new = stableTopologicalSort(rules, update)
        total2 += int(new[len(new)//2])

print('Part 1:', total1)
print('Part 2:', total2)