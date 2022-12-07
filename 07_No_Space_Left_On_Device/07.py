from collections import defaultdict

INPUT = "input"


def get_sizes_dict(lines):
    path_stack = []
    sizes_dict = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        if words[0] == "$":
            if words[1] == "cd" and words[2] == "..":
                path_stack.pop()
            elif words[1] == "cd":
                path_stack.append(words[2])
            elif words[1] == "ls":
                pass
            else:
                print("error: неучтенный случай c $")
        elif words[0] == "dir":
            pass
        elif words[0].isdigit():
            N = len(path_stack)
            size = int(words[0])
            for i in range(1, N + 1):
                path = ",".join(path_stack[:i])
                sizes_dict[path] += size
        else:
            print("error: неучтенный случай")

    return sizes_dict


def read_input():
    with open(INPUT, "r") as file:
        lines = file.read().strip().split("\n")
    return lines


def main():
    lines = read_input()
    sizes_dict = get_sizes_dict(lines)
    print(sum(filter(lambda x: x <= 100000, sizes_dict.values())))

    needed_space = 30000000 - (70000000 - sizes_dict["/"])
    print(list(filter(lambda x: x >= needed_space, sorted(sizes_dict.values())))[0])


if __name__ == "__main__":
    main()
