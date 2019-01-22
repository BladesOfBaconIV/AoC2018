from numpy import fromfunction, ndenumerate, vectorize

# Your puzzle input was 7400
SERIAL_NUMBER = 7400
SIZE_X, SIZE_Y = 300, 300

def get_power(x, y): # get the sum of the powers for slice grid[x:SIZE_X+1, y:SIZE_Y+1]
    RACK_ID = x + 10
    power = ((RACK_ID * y) + SERIAL_NUMBER) * RACK_ID
    power = (power % 1000) // 100
    return power - 5


grid = fromfunction(vectorize(get_power), (SIZE_X, SIZE_Y)).cumsum(axis=0).cumsum(axis=1)


# Seriously slow, needs optimising
max_power_square_size = []
for square_size in range(1, 35): # assuming less than 35
    print(square_size) # Takes a while 
    max_power = 0
    max_x, max_y = 0, 0
    for (x, y), p in ndenumerate(grid[:SIZE_X-square_size, :SIZE_Y-square_size]):
        power = grid[x, y] - grid[x+square_size, y] - grid[x, y+square_size] + grid[x+square_size, y+square_size]
        if power > max_power:
            max_power = power
            max_x, max_y = x, y
    max_power_square_size.append((square_size, (max_x, max_y), max_power))
# Part 1
part_1_max = max(max_power_square_size, key=lambda k: (k[0] == 3, k[2]))

# Part 2
part_2_max = max(max_power_square_size, key=lambda k: k[2] )

print("Part 1: ", part_1_max, "Part 2: ", part_2_max)