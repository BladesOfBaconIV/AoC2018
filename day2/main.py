from collections import Counter

with open('input.txt', 'r') as f:
    ids = [line.strip() for line in f.readlines()]

# part 1
number_of_two_repeats = 0
number_of_three_repeats = 0
for id in ids:
    letter_counts = Counter(id)
    number_of_two_repeats += 2 in letter_counts.values()
    number_of_three_repeats += 3 in letter_counts.values()
checksum = number_of_three_repeats * number_of_two_repeats

# part 2

for index, id_1 in enumerate(ids):
    for id_2 in ids[index+1:]:
        diff = [ord(char_1) - ord(char_2) != 0 for char_1, char_2 in zip(id_1, id_2)]
        if sum(diff) == 1: # assumes the most similar only differ by 1 letter
            part_2_ans = ''.join([letter for letter, different in zip(id_1, diff) if not different])
            break

print("Part 1: ", checksum, "Part 2: ", part_2_ans)