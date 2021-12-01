with open("input.txt") as f:
    p, i = float("inf"), 0
    for l in f:
        if int(l) > p:
            i += 1
        p = int(l)
    print(i)
