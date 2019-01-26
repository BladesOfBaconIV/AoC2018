import re
from string import ascii_lowercase

with open('input.txt', 'r') as f:
    polymer = f.readline().strip()

letters = '-' + ascii_lowercase

shortest_reduction = 10000000
part_1_ans = 0
for letter in letters:
    current_polymer = re.sub(letter.lower() + '|' + letter.upper(), '', polymer)
    print(letter)
    for char in polymer:
        current_polymer = re.sub(char.lower() + char.upper(), '', current_polymer)
        current_polymer = re.sub(char.upper() + char.lower(), '', current_polymer)
    # part 1
    if letter == '-':
        part_1_ans = len(current_polymer)
    # part 2
    shortest_reduction = len(current_polymer) if len(current_polymer) < shortest_reduction else shortest_reduction

print("Part 1: ", part_1_ans, "Part 2: ", shortest_reduction)
