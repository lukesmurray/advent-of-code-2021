d=open("input.txt").readlines()
print(sum([int(d[i])>int(d[i - 1])for i in range(len(d))]))
