from collections import deque, Counter

class Cart:

    def __init__(self, x_pos, y_pos, orientation):
        self.pos = complex(x_pos, y_pos)
        self.orientation = orientation
        self.turns = deque([1, 0, -1]) # paramters for turn_90_right func, 1 = right, 0 = straight, -1 = left

    def move(self):
        self.pos += self.orientation

    def turn_90_right(self, n=1):
        self.orientation *= 1j**n

    def get_current_turn(self):
        turn = self.turns[0]
        self.turns.rotate(1)
        return turn

    def get_x_y(self):
        return self.pos.real, self.pos.imag

    def check_collisions(self, list_of_carts):
        positions = [cart.pos for cart in list_of_carts]
        number_at_postions = Counter(positions)
        most_common_pos = number_at_postions.most_common(1)
        if number_at_postions[most_common_pos] == 2:
            crashed_carts = []
            for cart in list_of_carts:
                if cart.pos == most_common_pos:
                    crashed_carts.append(cart)
            return crashed_carts
        return None