from math import inf
from numpy import zeros, ndenumerate
from heapq import nsmallest
import re

with open('input.txt' ,'r') as f:
    coordinates = [tuple(map(int, re.findall(r'\d+', line.strip()))) for line in f.readlines()]

MAX_X = max(coordinates, key=lambda k: k[0])[0]
MAX_Y = max(coordinates, key=lambda k: k[1])[1]
space = zeros((MAX_X+1, MAX_Y+1))

coord_areas = dict([(coord, 0) for coord in coordinates])
area_within_10000 = 0
for (x, y), point_value in ndenumerate(space):
    distances = [abs(cx-x) + abs(cy-y) for cx, cy in coordinates] 
    coord_distances = zip(coordinates, distances)
    # Part 1
    shortest_2_distances = nsmallest(2, distances) # [(coord, distance), (coord, distance)]
    if shortest_2_distances[0] != shortest_2_distances[1]: # if two not points equally close
        closest_point, distance = min(coord_distances, key=lambda k: k[1])
        if x == 0 or x == MAX_X or y == 0 or y == MAX_Y: # if edge of space and set closest point area to inf
            coord_areas[closest_point] = inf
        coord_areas[closest_point] += 1
    # Part 2
    if sum(distances) < 10000:
        area_within_10000 += 1
# Part 1
for coord, area in coord_areas.items():
    coord_areas[coord] = 0 if area == inf else area
safest_point, largest_area = max(coord_areas.items(), key=lambda k: k[1])

print("Part 1: ", largest_area, "Part 2: ", area_within_10000)