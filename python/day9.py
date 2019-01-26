from collections import deque, defaultdict
from itertools import cycle

# INPUT: 463 players; last marble is worth 71787 points
NUM_PLAYERS = 463
HIGHEST_MARBLE = 71787

def play(highest_marble, num_players):
    marbles = range(1, highest_marble+1)
    circle = deque([0])
    scores = defaultdict(int)
    for marble, player in zip(marbles, cycle(range(1, NUM_PLAYERS+1))):
        if marble % 23 == 0:
            scores[player] += marble
            circle.rotate(-6)
            take = circle.popleft()
            scores[player] += take
        else:
            circle.rotate(2)
            circle.append(marble)
    return max(scores.items(), key=lambda k: k[1])

part_1_elf, part_1_score = play(HIGHEST_MARBLE, NUM_PLAYERS)
part_2_elf, part_2_score = play(HIGHEST_MARBLE*100, NUM_PLAYERS)

print("Part 1:", part_1_score, "Part 2:", part_2_score)
