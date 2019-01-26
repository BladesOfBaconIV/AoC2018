from numpy import zeros
import re

with open('input.txt', 'r') as f:
    changes = [line.strip() for line in f.readlines()]

GRID_X = 1000
GRID_Y = 1000

grid_1 = zeros((GRID_X, GRID_Y))
grid_2 = zeros((GRID_X, GRID_Y))
valid_ids = set()
for change in changes:
    id, x, y, width, height = map(int, re.findall(r'\d+', change))
    # part 1
    grid_1[x:x+width, y:y+height] += 1
    # part 2
    area_to_mark = grid_2[x:x+width, y:y+height]
    ids_in_area = set(area_to_mark.flatten())
    grid_2[x:x+width, y:y+height] = id
    if len(ids_in_area) > 1 or 0 not in ids_in_area: # if more than 1 id in area, ie. not just 0's, or 1 that isn't 0    
        valid_ids -= ids_in_area # remove any previously valid ids
    else:
        valid_ids.add(id)

overlapped_area = sum([square > 1 for square in grid_1.flatten()]) # part 1

print("Part 1: ", overlapped_area, "Part 2:", valid_ids)
