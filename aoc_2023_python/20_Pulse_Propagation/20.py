def get_config(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    config = {}
    for line in data:
        mod, dest_mods = line.strip().split(" -> ")
        dest_mods = dest_mods.split(", ")
        config[mod] = dest_mods
    return config


def get_answer_1(config):
    return


def main():
    config = get_config("test_input_1")
    print(config)
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
