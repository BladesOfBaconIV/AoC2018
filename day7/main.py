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
step_time = 0
graph = nx.DiGraph()
for u, v in edges:
    graph.add_edge(u, v, weight=ord(v)-64)
time = nx.dag_longest_path_length(graph)
nx.draw_networkx(graph)
plt.show()
print("Part 1:", step_order_single, "Part 2: ", time)