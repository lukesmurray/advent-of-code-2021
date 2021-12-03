# life_sup = ox_gen * co2_scrub


def bit_filter(data, index, tie_breaker, keep_most_common):
    keep = {"0": [], "1": []}
    value = 0
    for row in data:
        if row[index] == "1":
            keep["1"].append(row)
            value += 1
        else:
            keep["0"].append(row)
            value -=1
    if keep_most_common:
        result = "1" if value > 0 else "0" if value < 0 else tie_breaker
        return result, keep[result]
    else:
        result = "0" if value > 0 else "1" if value < 0 else tie_breaker
        return result, keep[result]


def ox_gen(data):
    keep = data
    num_bits = len(data[0])
    for bit_index in range(num_bits):
        result, keep = bit_filter(keep, bit_index, "1", True)
        if len(keep) == 1:
            return int(keep[0], 2)

def co2_scrub(data):
    keep = data
    num_bits = len(data[0])
    for bit_index in range(num_bits):
        result, keep = bit_filter(keep, bit_index, "0", False)
        if len(keep) == 1:
            return int(keep[0], 2)


d = [l.strip() for l in open('i')]
print(ox_gen(d) * co2_scrub(d))
