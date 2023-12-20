def get_config(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    config = {}
    for line in data:
        mod, dest_mods = line.strip().split(" -> ")
        if mod == "broadcaster":
            name = prefix = "broadcaster"
        else:
            prefix = mod[0]
            name = mod[1:]
        dest_mods = dest_mods.split(", ")
        config[name] = {"prefix": prefix, "dest_mods": dest_mods}
    return config


def get_answer_1(config):
    return


def main():
    config = get_config("test_input_1")
    print(config)
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
