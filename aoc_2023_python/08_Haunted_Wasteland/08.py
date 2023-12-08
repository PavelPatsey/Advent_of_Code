INPUT = "test_input"
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
        counter += 1
        key = nodes[key][follow_index]
    return counter


def get_answer_2(instruction, nodes):
    def _is_all_ends_z(keys_list):
        return all(map(lambda x: x.endswith("Z"), keys_list))

    counter = 0
    keys = [key for key in nodes.keys() if key.endswith("A")]
    len_instr = len(instruction)
    while not _is_all_ends_z(keys):
        index = counter % len_instr
        follow_index = FOLLOW_DICT[instruction[index]]
        counter += 1
        keys = [nodes[key][follow_index] for key in keys]
    return counter


def main():
    instruction, nodes = get_input()
    print(get_answer_1(instruction, nodes))
    print(get_answer_2(instruction, nodes))


if __name__ == "__main__":
    main()
