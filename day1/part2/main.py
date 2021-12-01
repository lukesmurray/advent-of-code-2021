d=[int(l)for l in open("input.txt").readlines()]
e=[sum(d[i-2:i+1])for i in range(2,len(d))]
print(sum([int(e[i])>int(e[i-1])for i in range(len(e))]))
