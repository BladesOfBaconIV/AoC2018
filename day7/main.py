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
# Going to try with graphs
# NetworkX has DiGraph module for directional graphs
