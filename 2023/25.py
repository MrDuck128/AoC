import networkx as nx

with open('25.txt') as f:
    data = f.read().splitlines()

graph = nx.Graph()
for line in data:
    left, right = line.split(': ')
    for node in right.split():
        graph.add_edge(left, node, capacity=1.0)

node1 = list(graph.nodes)[0]
for node in graph.nodes:
    if node != node1:
        cut, (a, b) = nx.minimum_cut(graph, node, node1)
        if cut == 3:
            print('Part 1:', len(a) * len(b))
            break