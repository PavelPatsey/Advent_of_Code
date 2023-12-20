from collections import deque
from copy import deepcopy


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
        pulse = None
        turn = None
        memory = None
        dest_mods = dest_mods.split(", ")
        if type_ == "%":
            config[name] = {
                "type": type_,
                "pulse": False,
                "turn": False,
                "dest_mods": dest_mods,
            }
        elif type_ == "&":
            config[name] = {
                "type": type_,
                "pulse": True,
                "memory": {},
                "dest_mods": dest_mods,
            }
        elif type_ == "broadcaster":
            config[name] = {
                "type": type_,
                "dest_mods": dest_mods,
            }
        else:
            assert False

    for name, module in config.items():
        for next_name in module["dest_mods"]:
            if config[next_name]["type"] == "&":
                config[next_name]["memory"][name] = False

    return config


def get_answer_1(config_):
    config = deepcopy(config_)
    N = 1
    l_p = 0
    h_p = 0
    for t in range(N):
        l_p += 1
        queue = deque([])
        for next_name in config["broadcaster"]["dest_mods"]:
            queue.append(("broadcaster", next_name, False))
        while queue:
            prev_name, name, pulse = queue.popleft()
            if pulse:
                h_p += 1
            else:
                l_p += 1
            module = config[name]

            # convert module
            if module["type"] == "%":
                if pulse is False:
                    if module["turn"]:
                        module["turn"] = module["pulse"] = False
                    else:
                        module["turn"] = module["pulse"] = True
            elif module["type"] == "&":
                module["memory"][prev_name] = pulse
                print(module["memory"].values())
                all_memory = all(module["memory"].values())
                module["pulse"] = False if all_memory else True
            else:
                assert False

            next_pulse = module["pulse"]
            for next_name in module["dest_mods"]:
                queue.append((name, next_name, next_pulse))

    return h_p * l_p


def main():
    config = get_config("test_input_1")
    print(config)
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
