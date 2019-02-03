from numpy import zeros
from Cart import Cart

with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

track_map = zeros((max(map(len, lines)), len(lines)))
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
    'v': 1j,
    '>': 1,
    '^': -1j,
    '<': -1
}
for line_num, line in enumerate(lines):
    for char_num, char in enumerate(line):
        if char in possible_carts:
            carts.append(Cart(char_num, line_num, possible_carts[char]))
            track_map[char_num, line_num] = 1
        else:
            track_map[char_num, line_num] = track_conversion_dict[char]

removed_carts = []
while len(carts) != 1:
    for cart in carts:
        track = track_map[cart.get_x_y()]
        if track == 2:
            if cart.orientation.imag:
                cart.turn_90_right(3)
            else:
                cart.turn_90_right()
        elif track == 3:
            if cart.orientation.imag:
                cart.turn_90_right()
            else:
                cart.turn_90_right(3)
        elif track == 4:
            cart.turn_90_right(cart.get_current_turn())
        cart.move()
        removed_carts.extend(carts[0].remove_crashed(carts))
    

print(removed_carts[0].get_x_y(), carts[0].pos)
