import networkx as nx
import matplotlib.pyplot as plt
import re

with open('input.txt', 'r') as f:
    points = [tuple(map(int, re.findall(r'-\d+|\d+', line))) for line in f.readlines()]

def distance(p1, p2):
    return sum([abs(d1 - d2) for d1, d2 in zip(p1, p2)])

space = nx.Graph()
for p in points:
    space.add_node(p)
    for node in space.nodes:
        if distance(p, node) <= 3:
            space.add_edge(node, p)

print(len([g for g in nx.connected_component_subgraphs(space)]))