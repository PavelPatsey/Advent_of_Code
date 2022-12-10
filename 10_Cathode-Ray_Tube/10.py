INPUT = "test_input"


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
    print(list(enumerate(values)))
    print()
    
    print(list(filter(lambda x: (x[0]-20)%40==0, enumerate(values))))
    print()
    print(list(map(lambda x: (x[0])*x[1], filter(lambda x: (x[0]+1-20)%40==0, enumerate(values)))))

    print(sum(list(map(lambda x: x[0]*x[1], filter(lambda x: (x[0]+1-20)%40==0, enumerate(values))))))



if __name__ == "__main__":
    main()
