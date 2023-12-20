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


def get_converted_module(module, input_pulse):
    if module["type"] == "broadcaster":
        return module

    new_module = dict(module)
    pulse = new_module["pulse"]
    memory = new_module["memory"]
    turn = new_module["turn"]

    if module["type"] == "%":
        if not input_pulse:
            if turn:
                turn = pulse = False
            else:
                turn = pulse = True
    elif module["type"] == "&":
        # rework here
        pass
        # memory.append(input_pulse)
        #     memory = input_pulse
        # elif memory:
        #     memory = input_pulse
        # elif not memory:
        #     pass
        # else:
        #     assert False
        # pulse = not memory
    else:
        assert False

    new_module["memory"] = memory
    new_module["pulse"] = pulse
    new_module["turn"] = turn
    return new_module


def get_answer_1(config_):
    config = deepcopy(config_)
    N = 1
    l_p = 0
    h_p = 0
    for t in range(N):
        l_p += 1
        queue = deque(
            [
                ("broadcaster", module_name, False)
                for module_name in config["broadcaster"]["dest_mods"]
            ]
        )
        print(queue)
        while queue:
            print(queue)
            prev_name, name, pulse = queue.popleft()
            if pulse:
                h_p += 1
            else:
                l_p += 1
            module = config[name]
            new_module = get_converted_module(module, pulse)
            config[name] = new_module
            next_pulse = new_module["pulse"]
            for next_name in new_module["dest_mods"]:
                queue.append((name, next_name, next_pulse))

    return h_p * l_p


def main():
    config = get_config("test_input_1")
    print(config)
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
