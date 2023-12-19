def get_workflows(input_file):
    with open(input_file, "r") as file:
        data = file.read()

    workflows_list = data.strip().split("\n\n")[0].splitlines()
    workflows = {}
    for line in workflows_list:
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    return workflows


def count(workflows, ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product

    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]

        if cmp == "<":
            left = (lo, min(n - 1, hi))
            right = (max(n, lo), hi)
        else:
            left = (max(n + 1, lo), hi)
            right = (lo, min(n, hi))

        assert left[0] <= left[1] and right[0] <= right[1]
        ranges = dict(ranges)
        ranges[key] = left
        total += count(workflows, ranges, target)

        ranges = dict(ranges)
        ranges[key] = right

    else:
        total += count(workflows, ranges, fallback)

    return total


def main():
    workflows = get_workflows("input")
    ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    print(count(workflows, ranges))


if __name__ == "__main__":
    main()
