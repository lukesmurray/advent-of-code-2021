d = open("input.txt").readlines()
s = sum([1 for i, x in enumerate(d) if int(x) > int(d[i - 1])])
print(s)
