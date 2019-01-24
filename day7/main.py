import networkx as nx
import matplotlib.pyplot as plt
import re

with open('input.txt', 'r') as f:
    step_requirements = {}
    edges = []
    for line in f:
        requirement, step = re.findall(r'(?<=tep )\w', line)
        step_requirements.setdefault(step, set()).add(requirement)
        edges.append((requirement, step))
start_steps = set([r for rs in step_requirements.values() for r in rs if r not in step_requirements])
step_requirements.update([(start, set()) for start in start_steps])

# Part 1
step_order_single = ''
while len(step_order_single) < len(step_requirements):
    possible_steps = set()
    for step, requirements in step_requirements.items():
        if requirements.issubset(set(step_order_single)) and step not in step_order_single:
            possible_steps.add(step)
    step_order_single += min(possible_steps)

# Part 2
step_time = 60
num_workers = 5
graph = nx.DiGraph()
for v, u in edges:
    graph.add_edge(u, v)

for node in graph.nodes:
    graph.nodes[node]['work'] = ord(node) - 64 + step_time

time = 0
while graph.nodes:
    possible_steps = sorted([n for n in graph.nodes if not graph.in_degree(n)]
                            , key=lambda n: graph.nodes[n]['work'])
    for worker, node in zip(range(num_workers), possible_steps):
        graph.nodes[node]['work'] -= 1

        if not graph.nodes[node]['work']:
            graph.remove_node(node)
    time += 1

print("Part 1: ", step_order_single, "Part 2: ", time)