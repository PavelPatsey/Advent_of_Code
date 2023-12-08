INPUT = "input"
FOLLOW_DICT = {"L": 0, "R": 1}


def get_input():
    with open(INPUT, "r") as file:
        data = file.read()
    instruction, nodes_str = data.split("\n\n")
    nodes = {}
    for line in nodes_str.strip().split("\n"):
        key, value = line.split(" = ")
        value = value.strip("()").split(", ")
        nodes[key] = value

    return instruction, nodes


def get_answer_1(instruction, nodes):
    counter = 0
    key = "AAA"
    len_instr = len(instruction)
    while not key == "ZZZ":
        index = counter % len_instr
        follow_index = FOLLOW_DICT[instruction[index]]
        key = nodes[key][follow_index]
        counter += 1
    return counter


def main():
    instruction, nodes = get_input()
    print(get_answer_1(instruction, nodes))


if __name__ == "__main__":
    main()
