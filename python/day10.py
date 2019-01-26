import matplotlib.pyplot as plt
import re

with open('input.txt', 'r') as f:
    points = []
    velocities = []
    for line in f.readlines():
        px, py, vx, vy = map(int, re.findall(r'-\d+|\d+', line.strip()))
        points.append((px, -1*py)) # Reversing y as -y is upwards
        velocities.append((vx, -1*vy))


time = 0
while len(set(points)) > 200: # while there is more than 100 unique points
    points = list(map(lambda x, y: (x[0] + y[0], x[1] + y[1]), points, velocities)) # update the points
    time+=1

# Part 1
plt.scatter(*zip(*points))
plt.show()

#Part 2
print("Message Appears at {} seconds".format(time))