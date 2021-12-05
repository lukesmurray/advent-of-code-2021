is_vertical = lambda l: l[1] == l[3]
is_horizontal = lambda l: l[0] == l[2]

def get_points(l):
    x_step = 1 if l[0] < l[2] else -1
    y_step = 1 if l[1] < l[3] else -1
    return [
        f"{x},{y}"
        for x in range(l[0], l[2] + x_step, x_step)
        for y in range(l[1], l[3] + y_step, y_step)
    ]

lines = [
    [int(coord) for point in line.strip().split(" -> ") for coord in point.split(",")]
    for line in open("i")
]
lines = [l for l in lines if is_horizontal(l) or is_vertical(l)]


vents = {}
for line in lines:
    for point in get_points(line):
        vents[point] = vents.get(point, 0) + 1

print(len([v for v in vents.values() if v > 1]))

