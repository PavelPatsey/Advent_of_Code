INPUT = "input"


def get_CRT_rows(values):
    CRT_row = ""
    CRT_rows = []
    for i in range(1, 240 + 1):
        pixel_position = (i - 1) % 40
        if pixel_position in (values[i] - 1, values[i], values[i] + 1):
            CRT_row += "#"
        else:
            CRT_row += "."
        if pixel_position == 39:
            CRT_rows.append(CRT_row)
            CRT_row = ""

    return CRT_rows


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

    filtered = filter(lambda x: (x[0] - 20) % 40 == 0, enumerate(values))
    mapped = map(lambda x: x[0] * x[1], filtered)
    print(sum(mapped))

    CRT_rows = get_CRT_rows(values)
    for row in CRT_rows:
        print(row)


if __name__ == "__main__":
    main()
