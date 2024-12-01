from collections import Counter


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
        a, b = [], []
        for d in data:
            n = d.split()
            a.append(int(n[0]))
            b.append(int(n[1]))
    return a, b


def get_answer_1(a, b):
    _a = sorted(a)
    _b = sorted(b)
    res = 0
    for i, j in zip(_a, _b):
        res += abs(i - j)
    return res


def get_answer_2(a, b):
    counter = Counter(b)
    return sum(x * counter[x] for x in a)


def main():
    a, b = get_data("input")
    print(get_answer_1(a, b))
    print(get_answer_2(a, b))


if __name__ == "__main__":
    main()
