from collections import deque

with open('input.txt', 'r') as f:
    info_stream = deque([int(n) for n in f.readline().split(' ')])

meta_data = []
while info_stream:
    print(info_stream)
    number_child_nodes = info_stream[0]
    if not number_child_nodes:
        info_stream.popleft()
        meta_count = info_stream.popleft()
        for i in range(meta_count):
            meta_data.append(info_stream.popleft())
        info_stream.rotate(2)
        info_stream[0] -= 1
    else:
        info_stream.rotate(-2)
print(meta_data)
