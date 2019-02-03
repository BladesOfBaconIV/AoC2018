from collections import deque, Counter

class Cart:

    def __init__(self, x_pos, y_pos, orientation):
        self.pos = complex(x_pos, y_pos)
        self.orientation = orientation
        self.turns = deque([-1, 0, 1]) # paramters for turn_90_right func, 1 = right, 0 = straight, -1 = left

    def move(self):
        self.pos += self.orientation

    def turn_90_right(self, n=1):
        self.orientation *= 1j**n

    def get_current_turn(self):
        turn = self.turns[0]
        self.turns.rotate(-1)
        return turn

    def get_x_y(self):
        return int(self.pos.real), int(self.pos.imag)

    def remove_crashed(self, list_of_carts):
        crashed_carts = []
        for cart_num, current_cart in enumerate(list_of_carts):
            for cart in list_of_carts[cart_num+1:]:
                if cart.orientation == current_cart.orientation:
                    continue
                if cart.pos == current_cart.pos:
                    crashed_carts.append(cart)
                    crashed_carts.append(current_cart)
        for cart in set(crashed_carts):
            list_of_carts.remove(cart)
        return crashed_carts