def get_sequence(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    return data[0].strip().split(",")


def get_hash(string):
    value = 0
    for ch in string:
        value = (value + ord(ch)) * 17 % 256
    return value


def get_answer_1(sequence):
    return sum(map(get_hash, sequence))


def get_answer_2(sequence):
    boxes = [[] for _ in range(256)]
    for item in sequence:
        if "=" in item:
            label, value = item.split("=")
            lenses = boxes[get_hash(label)]
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    lenses[i][1] = int(value)
                    break
            else:
                lenses.append([label, int(value)])
        elif "-" in item:
            label, _ = item.split("-")
            lenses = boxes[get_hash(label)]
            for i in range(len(lenses)):
                if lenses[i][0] == label:
                    del lenses[i]
                    break
        else:
            assert False

    result = 0
    for b in range(len(boxes)):
        for i in range(len(boxes[b])):
            result = result + (b + 1) * (i + 1) * boxes[b][i][1]
    return result


def main():
    sequence = get_sequence("input")
    print(get_answer_1(sequence))
    print(get_answer_2(sequence))


if __name__ == "__main__":
    main()
