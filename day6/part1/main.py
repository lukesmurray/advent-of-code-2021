*data, counts = [*map(int, open("i").read().split(",")), {}]
[counts.update({i: counts.get(i, 0) + 1}) for i in data]


def simulate_day(counts):
    new_count = {}
    for days, count in counts.items():
        if days == 0:
            new_count[6] = new_count.get(6, 0) + count
            new_count[8] = new_count.get(8, 0) + count
        else:
            new_count[days - 1] = new_count.get(days - 1, 0) + count
    return new_count


for i in range(80):
    counts = simulate_day(counts)

print(sum(counts.values()))
