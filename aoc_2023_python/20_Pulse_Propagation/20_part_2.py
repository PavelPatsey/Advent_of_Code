from collections import deque
from copy import deepcopy
import math


def get_config(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    config = {}
    for line in data:
        mod, outputs = line.strip().split(" -> ")
        if mod == "broadcaster":
            name = type_ = "broadcaster"
        else:
            type_ = mod[0]
            name = mod[1:]
        outputs = outputs.split(", ")
        if type_ == "%":
            config[name] = {
                "type": type_,
                "pulse": False,
                "turn": False,
                "outputs": outputs,
            }
        elif type_ == "&":
            config[name] = {
                "type": type_,
                "pulse": True,
                "memory": {},
                "outputs": outputs,
            }
        elif type_ == "broadcaster":
            config[name] = {
                "type": type_,
                "outputs": outputs,
            }
        else:
            assert False

    for name, module in config.items():
        for next_name in module["outputs"]:
            if next_name in config and config[next_name]["type"] == "&":
                config[next_name]["memory"][name] = False

    return config


def get_answer_1(config_):
    config = deepcopy(config_)

    module_to_rx = [name for name, module in config.items() if "rx" in module["outputs"]][0]
    cycle_lengths = {}
    seen = {name: 0 for name, module in config.items() if module_to_rx in module["outputs"]}

    presses = 0
    answer_is_found = False
    while not answer_is_found:
        presses += 1
        queue = deque([])
        for next_name in config["broadcaster"]["outputs"]:
            queue.append(("broadcaster", next_name, False))
        while queue:
            prev_name, name, pulse = queue.popleft()

            if name not in config:
                continue
            module = config[name]

            if name == module_to_rx and pulse is True:
                seen[prev_name] += 1
                print(f"{seen=}")
                print(f"{cycle_lengths=}")

                if prev_name not in cycle_lengths:
                    cycle_lengths[prev_name] = presses
                else:
                    print("else", f"{seen[prev_name]=}")
                    print("else", f"{cycle_lengths[prev_name]=}")
                    assert presses == seen[prev_name] * cycle_lengths[prev_name]

                print(f"{seen.values()}=")

                if all(seen.values()):
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = x * cycle_length // math.gcd(x, cycle_length)
                    answer_is_found = True

            if module["type"] == "%":
                if pulse is False:
                    if module["turn"]:
                        module["turn"] = module["pulse"] = False
                    else:
                        module["turn"] = module["pulse"] = True
                    next_pulse = module["pulse"]
                    for next_name in module["outputs"]:
                        queue.append((name, next_name, next_pulse))
            elif module["type"] == "&":
                module["memory"][prev_name] = pulse
                all_memory = all(module["memory"].values())
                module["pulse"] = False if all_memory else True

                next_pulse = module["pulse"]
                for next_name in module["outputs"]:
                    queue.append((name, next_name, next_pulse))

            else:
                assert False
    return x


def main():
    config = get_config("input")
    print(get_answer_1(config))


if __name__ == "__main__":
    main()
