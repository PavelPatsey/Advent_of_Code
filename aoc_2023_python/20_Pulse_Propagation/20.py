from collections import deque


def get_config(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    config = {}
    for line in data:
        mod, dest_mods = line.strip().split(" -> ")
        if mod == "broadcaster":
            name = type_ = "broadcaster"
        else:
            type_ = mod[0]
            name = mod[1:]
        dest_mods = dest_mods.split(", ")
        config[name] = {
            "type": type_,
            "pulse": False,
            "dest_mods": dest_mods,
            "memory": [],
        }
        return config

    def get_converted_module(module, pulse):
        """
        module = {"type_": type_, "pulse": False, "dest_mods": dest_mods, "memory": []}
        """
        if module["type"] == "broadcaster":
            return module
        elif module["type"] == "%":
            pass
        elif module["type"] == "&":
            pass
        else:
            assert False

    def get_answer_1(config):
        N = 1000
        l_p = 0
        h_p = 0
        for _ in range(N):
            queue = deque(["broadcaster"])
            while queue:
                name = queue.popleft()
                module = config[name]
                pulse = module["pulse"]
                if pulse:
                    h_p += 1
                else:
                    l_p += 1
                new_module = get_converted_module(module, pulse)
                queue = queue + deque(new_module["dest_mods"])

    def main():
        config = get_config("test_input_1")
        print(config)
        print(get_answer_1(config))

    if __name__ == "__main__":
        main()
