with open("input.txt") as f:
    data = [int(s) for s in f.read().splitlines()]
    prev = float("inf")
    increased = 0
    for value in data:
        if value > prev:
            increased += 1
        prev = value
    print(increased)
