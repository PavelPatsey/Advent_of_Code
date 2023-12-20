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
        if type_ == "%":
            pulse = False
            turn = False
        if type_ == "%":
            pulse = True
            turn = False
        else:
            pass
        dest_mods = dest_mods.split(", ")
        config[name] = {
            "type": type_,
            "pulse": pulse,
            "turn": turn,
            "dest_mods": dest_mods,
            "memory": memory,
        }
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
        if memory is None:
            memory = input_pulse
        elif memory:
            memory = input_pulse
        elif not memory:
            pass
        else:
            assert False
        pulse = not memory
    else:
        assert False

    new_module["memory"] = memory
    new_module["pulse"] = pulse
    new_module["turn"] = turn
    return new_module


def is_all_triggers_turn_off(config):
    all_triggers_turn_off = True
    for module in config.values():
        if module["type"] == "%" and not module["turn"]:
            all_triggers_turn_off = False
            break
    return all_triggers_turn_off


def get_answer_1(config_):
    config = deepcopy(config_)
    N = 1
    l_p = 0
    h_p = 0
    for t in range(N):
        queue = deque(["broadcaster"])
        while queue:
            name = queue.popleft()

            if is_all_triggers_turn_off(config) and t != 0:
                print(t)
                break

            module = config[name]
            pulse = module["pulse"]
            if pulse:
                h_p += 1
            else:
                l_p += 1
            new_module = get_converted_module(module, pulse)
            config[name] = new_module
            queue = queue + deque(new_module["dest_mods"])

    return h_p * l_p


def main():
    config = get_config("test_input_1")
    print(config)
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
