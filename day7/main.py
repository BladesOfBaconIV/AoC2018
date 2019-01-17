from heapq import nsmallest
import re

with open('input.txt', 'r') as f:
    step_requirements = {}
    for line in f:
        requirement, step = re.findall(r'(?<=tep )\w', line)
        step_requirements.setdefault(step, set()).add(requirement)
start_steps = set([r for rs in step_requirements.values() for r in rs if r not in step_requirements])
step_requirements.update([(start, set()) for start in start_steps])

def get_step_order(workers, step_time):
    worker_info = [[i, 0, ''] for i in range(workers)] # (worker number, time till free, working on)
    step_order = ''
    time = 0
    taken = set()
    while time < 20: # len(step_order) < len(step_requirements):
        step_order += ''.join([wo for wn, tf, wo in worker_info if tf == time]) 
        possible_steps = set()
        for step, requirements in step_requirements.items():
            if requirements.issubset(set(step_order)) and step not in taken:
                possible_steps.add(step)
        for worker_num, time_free, working_on in worker_info:
            if time_free == time:
                step_order += working_on
                if possible_steps:
                    worker_info[worker_num][2] = min(possible_steps)
                    taken.add(min(possible_steps))
                    worker_info[worker_num][1] += ord(worker_info[worker_num][2]) + step_time - 64
                    possible_steps.remove(worker_info[worker_num][2])
                else:
                    worker_info[worker_num][2] = ''
        print(time, worker_info, step_order)
        time += 1
    return step_order, time

#part_1_order, part_1_time = get_step_order(1, 0)
part_2_order, part_2_time = get_step_order(2, 0)
print(part_2_order)
#print("Part 1: ", part_1_order, "Part 2: ", part_2_time)
