with open('input.txt') as f:
    horizontal = depth = aim = 0
    d = [[x, int(y)] for x, y in [x.split(' ') for x in f.read().splitlines()]]
    for direction, amount in d:
        if direction == "forward":
            horizontal += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    print(horizontal * depth)
