import matplotlib.pyplot as plt
from math import sqrt
from numpy import sign
from heapq import nlargest
import re

with open('input.txt', 'r') as f:
    points = []
    velocities = []
    for line in f.readlines():
        px, py, vx, vy = map(int, re.findall(r'-\d+|\d+', line.strip()))
        points.append((px, -1*py))
        velocities.append((vx, -1*vy))

#top_left_point, bottom_right = nlargest(2, points, key=lambda k: sqrt(k[0]**2 + k[1]**2)*-1*sign(k[0], k[1]))
#print(top_left_point, bottom_right)
time = 0
while len(set(points)) > 200: # while there is more than 100 unique points
    points = list(map(lambda x, y: (x[0] + y[0], x[1] + y[1]), points, velocities)) # update the points
    time+=1

# Part 1
plt.scatter(*zip(*points))
plt.show()

#Part 2
print("Message Appears at {} seconds".format(time))