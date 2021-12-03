d = [l.strip() for l in open('i')]
bits = [0] * len(d[0])
for l in d:
    for i, c in enumerate(l.strip()):
        bits[i] += 1 if c == "1" else -1
bits = [1 if g > 0 else 0 for g in bits]
gamma = int(''.join(map(str, bits)), 2)
epsilon = int(''.join(map(str, [1 - b for b in bits])), 2)
print(gamma * epsilon)



