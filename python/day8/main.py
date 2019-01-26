# Solution based on u/sciyoshi's solution from
# https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/

with open('input.txt', 'r') as f:
    info_stream = [int(n) for n in f.readline().split()]

def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for _ in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )

total, value, remaining = parse(info_stream)

print("Part 1: ", total, "Part 2: ", value)