def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
        a,b = [], []
        for d in data:
            n = d.split()
            a.append(int(n[0]))
            b.append(int(n[1]))
    return a,b


def get_answer_1(a, b):
    a.sort()
    b.sort()
    print(a,b)
    res = 0
    for i,j in zip(a,b):
        print(abs(i-j))
        res += abs(i-j)
    return res



def main():
    a,b = get_data("input")
    print(a,b)
    print(get_answer_1(a,b))


if __name__ == "__main__":
    main()
