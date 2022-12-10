INPUT = "input"


def get_values(commands):
    x = 1
    values = [x]

    for command in commands:
        if "noop" in command:
            values.append(x)
        elif "addx" in command:
            values.append(x)
            values.append(x)
            x += int(command.strip().split()[1])
        else:
            print("error!")

    return values


def read_input():
    with open(INPUT, "r") as file:
        commands = file.readlines()
    return commands


def main():
    commands = read_input()
    values = get_values(commands)
    print(list(enumerate(values)))

    filtered = filter(lambda x: (x[0] - 20) % 40 == 0, enumerate(values))
    mapped = map(lambda x: x[0] * x[1], filtered)
    print(sum(mapped))

    str_stack = ""
    for i in range(1, 240 + 1):
        I = (i - 1) % 40
        if I in (values[i] - 1, values[i], values[i] + 1):
            str_stack += "#"
        else:
            str_stack += "."
        if I == 39:
            print(str_stack)
            str_stack = ""

    # print(str_stack)


if __name__ == "__main__":
    main()
