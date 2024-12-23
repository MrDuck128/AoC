import networkx as nx

with open('23.txt') as f:
    connections = [line.split('-') for line in f.read().splitlines()]

G = nx.Graph()

for start, end in connections:
    G.add_edge(start, end)

print('Part 1:', sum(len(c) == 3 and any(pc[0] == 't' for pc in c) for c in nx.enumerate_all_cliques(G)))

print('Part 2:', ','.join(sorted(max(nx.find_cliques(G), key=len))))