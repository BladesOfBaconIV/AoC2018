from collections import Counter
import re

with open('input.txt', 'r') as f:
    log_lines = [line.strip() for line in f]
log_lines.sort()

# makes dict of {guard_id: [minutes asleep]}
guard_sleep_times = {}
current_guard = 0
while log_lines:
    current_line = log_lines.pop(0)
    if 'Guard' in current_line:
        current_guard = int(re.findall(r'(?<=#)\d+', current_line)[0])
    else:
        start_sleep = int(re.findall(r'(?<=:)\d+', current_line)[0])
        end_sleep = int(re.findall(r'(?<=:)\d+', log_lines.pop(0))[0])
        guard_sleep_times.setdefault(current_guard, []).extend(range(start_sleep, end_sleep))

# part 1
sleepiest_guard, times_asleep = max(guard_sleep_times.items(), key=lambda k: len(k[1]))
most_common_sleep_minute = Counter(times_asleep).most_common(1)[0][0] # [(minute, frequency)]
part_1_ans = sleepiest_guard * most_common_sleep_minute

# part 2
most_common_guard, times_asleep = max(guard_sleep_times.items(), key=lambda k: Counter(k[1]).most_common(1)[0][1])
most_common_minute = Counter(times_asleep).most_common(1)[0][0]
part_2_ans = most_common_guard * most_common_minute
print(most_common_guard, most_common_minute)

print("Part 1: ", part_1_ans, "Part 2: ", part_2_ans)