d = open("input.txt").readlines()
s = sum([int(d[i]) > int(d[i - 1]) for i in range(len(d))])
print(s)
