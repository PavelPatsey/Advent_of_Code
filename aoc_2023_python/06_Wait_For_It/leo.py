def parse(infile):
    with open(infile) as f:
        inp = f.read()
        lines = inp.split('\n')
        pairs = [line.split() for line in lines]
        pairs = [(comb, int(strength)) for comb, strength in pairs]
        return pairs


VALS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def get_str(s):
    vals = [VALS[c] - 2 for c in s]
    base_str = 0
    for v in vals:
        base_str *= 13
        base_str += v

    freq = [0] * 13
    for val in vals:
        freq[val] += 1

    ff = sorted(filter(None, freq))
    # print(ff)
    if ff == [5]:
        st = 7000000
    elif ff == [1, 4]:
        st = 6000000
    elif ff == [2, 3]:
        st = 5000000
    elif ff == [1, 1, 3]:
        st = 4000000
    elif ff == [1, 2, 2]:
        st = 3000000
    elif ff == [1, 1, 1, 2]:
        st = 2000000
    elif ff == [1, 1, 1, 1, 1]:
        st = 1000000
    else:
        st = 0
    return base_str + st


VALS2 = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


def get_str2(s):
    vals = [VALS[c] - 2 for c in s]
    vals2 = [VALS2[c] - 1 for c in s]
    print(vals)
    print(vals)
    base_str = 0
    for v in vals2:
        base_str *= 13
        base_str += v

    freq = [0] * 13
    for val in vals:
        freq[val] += 1

    freq_j = freq[9]
    freq[9] = 0
    print(freq)
    maxi = freq.index(max(freq))
    freq[maxi] += freq_j
    print(freq)
    ff = sorted(filter(None, freq))
    print(ff)
    if ff == [5]:
        st = 7000000
    elif ff == [1, 4]:
        st = 6000000
    elif ff == [2, 3]:
        st = 5000000
    elif ff == [1, 1, 3]:
        st = 4000000
    elif ff == [1, 2, 2]:
        st = 3000000
    elif ff == [1, 1, 1, 2]:
        st = 2000000
    elif ff == [1, 1, 1, 1, 1]:
        st = 1000000
    else:
        st = 0

    return base_str + st


def solve1(infile):
    pairs = parse(infile)
    pairs.sort(key=lambda x: get_str(x[0]))
    print(pairs)
    ans = 0
    for i, (c, v) in enumerate(pairs):
        ans += (i + 1) * v
    return ans


def solve2(infile):
    pairs = parse(infile)
    pairs.sort(key=lambda x: get_str2(x[0]))
    print(pairs)
    ans = 0
    for i, (c, v) in enumerate(pairs):
        ans += (i + 1) * v
    return ans


def main():
    # print(solve1('7_test.in'))
    # print(solve1('7.in'))
    # print(solve2('7_test.in'))
    print(solve2('7.in'))


if __name__ == '__main__':
    main()