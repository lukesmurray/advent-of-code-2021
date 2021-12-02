d=[int(l)for l in open("i")]
print(sum([d[i]>d[i-1]for i in range(len(d))]))
