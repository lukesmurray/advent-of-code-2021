with open('input.txt') as f:
    horizontal = depth = 0
    d = [[x, int(y)] for x, y in [x.split(' ') for x in f.read().splitlines()]]
    for direction, amount in d:
        if direction == "forward":
            horizontal += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount
    print(horizontal * depth)
