d=[int(l)for l in open("input.txt")]
print(sum([int(d[i])>int(d[i-3])for i in range(3, len(d))]))
