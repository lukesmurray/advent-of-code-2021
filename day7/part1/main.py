d = list(map(int, open("i").read().split(",")))
f = lambda p, d: sum([abs(l - p) for l in d])
r = [f(p, d) for p in range(min(d), max(d) + 1)]
print(min(r))
