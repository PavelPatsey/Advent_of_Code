INPUT = "input"


def get_values(commands):
    x = 1
    values = [x]

    for command in commands:
        if "noop" in command:
            values.append(x)
        elif "addx" in command:
            values.append(x)
            x += int(command.strip().split()[1])
            values.append(x)
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

    filtered = filter(lambda x: (x[0] + 1 - 20) % 40 == 0, enumerate(values))
    mapped = map(lambda x: (x[0] + 1) * x[1], filtered)
    print(sum(mapped))


if __name__ == "__main__":
    main()
