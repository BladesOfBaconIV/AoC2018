import re

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

plant_pattern = re.compile(r'[#.]+') # more efficient as pattern only needs to be compiled once
initial = re.findall(plant_pattern, lines.pop(0))[0]
lines.pop(0) # remove the blank line
rules = {}
for line in lines:
    rule, result = re.findall(plant_pattern, line)
    rules[rule] = result

def apply_generation(plants):
    new_gen = ''
    plants = '..' + plants + '..'
    for index, plant in enumerate(plants[2:-2]):
        subsection = plants[index-2:index+3]
        if subsection in rules:
            new_gen += rules[subsection]
        else:
            new_gen += plant
    return new_gen

padding = 0
initial = '...' + initial + '...'
for gen in range(21):
    print(gen, initial)
    initial = apply_generation(initial)
print(sum([i-3 for i, p in enumerate(initial) if p == '#']))