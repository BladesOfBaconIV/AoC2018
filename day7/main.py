import networkx as nx
import re

with open('input.txt', 'r') as f:
    step_requirements = {}
    for line in f:
        requirement, step = re.findall(r'(?<=tep )\w', line)
        step_requirements.setdefault(step, set()).add(requirement)
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
graph.add_node(0) # start point
while len(graph.nodes()) < len(step_requirements):
    for step, requirements in step_requirements.items():
        if requirements == None:
            continue
        if requirements == set(): # add steps with no requirements
            print("Adding step: ", step, requirements)
            graph.add_node(step)
            graph.add_edge(0, step, weight=ord(step)-64+step_time)
            step_requirements[step] = None
        elif requirements.issubset(set(graph.nodes())): # add graph with all requirements completed
            print("Adding step: ", step, requirements)
            graph.add_node(step)
            graph.add_edge(list(requirements)[0], step, weight=ord(step)-64+step_time)
            step_requirements[step] = None # remove node from list
        for remaining_steps, remaining_req in step_requirements.items():
            for node in graph.nodes():
                if remaining_req != None and len(remaining_req) > 1 and node in remaining_req:
                    step_requirements[remaining_steps].remove(node)
time = nx.dag_longest_path_length(graph)
nx.draw_networkx(graph)
print("Part 1:", step_order_single, "Part 2: ", time)