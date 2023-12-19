def get_parsed_input(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    x = "x"
    m = "m"
    a = "a"
    s = "s"
    workflows, parts = data.strip().split("\n\n")
    workflows = workflows.split()
    workflows_dict = {}
    for line in workflows:
        key, value = line.split("{")
        value = value.replace("}", "")
        value = value.split(",")
        workflows_dict[key] = value

    parts = parts.split()
    parts_list = []
    for line in parts:
        line = line.replace("=", ":")
        parts_list.append(eval(line))

    return workflows_dict, parts_list


def is_accepted(part, workflows):
    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]

    key = "in"
    i = 0
    while key not in ("A", "R"):
        value = workflows[key][i]
        if ":" in value:
            condition, go_to = value.split(":")
            condition = eval(condition)
            if condition:
                key = go_to
                i = 0
            else:
                i += 1
        else:
            key = value
            i = 0
    return True if key == "A" else False


def get_answer_1(workflows, parts):
    filtered = filter(lambda x: is_accepted(x, workflows) is True, parts)
    return sum(map(lambda x: sum(x.values()), filtered))


def main():
    workflows, parts = get_parsed_input("input")
    print(f"{workflows=}")
    print(f"{parts=}")
    print(get_answer_1(workflows, parts))


if __name__ == "__main__":
    main()
