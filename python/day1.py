from itertools import cycle

with open('input.txt', 'r') as f:
    deltas = [int(line.strip()) for line in f.readlines()]

# part 1
part_1_ans = sum(deltas)

# part 2
previous_frequencies = {0}
current_frequency = 0
for delta in cycle(deltas):
    current_frequency += delta
    if current_frequency in previous_frequencies:
        break
    previous_frequencies.add(current_frequency)

print("Part 1: ", part_1_ans, "Part 2: ", current_frequency)