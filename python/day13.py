from numpy import zeros
from Cart import Cart

with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

print(len(lines))

track_map = zeros((len(lines), max(map(len, lines))))
carts = []
track_conversion_dict = {
    ' ': 0,
    '-': 1,
    '|': 1,
    '\\': 2,
    '/': 3,
    '+': 4
}
possible_carts = {
    'v': -1j,
    '>': 1,
    '^': 1j,
    '<': -1
}
for line_num, line in enumerate(lines):
    for char_num, char in enumerate(line):
        if char in possible_carts:
            carts.append(Cart(char_num, line_num, possible_carts[char]))
            track_map[char_num, line_num] = 1
        else:
            track_map[char_num, line_num] = track_conversion_dict[char]

while len(carts) > 1:
    for cart in carts:
        track = track_map[cart.get_x_y()]
        if track == 1: # if the track its on isn't a bend
            cart.move()
        elif track == 2:
            if cart.orientation == 
