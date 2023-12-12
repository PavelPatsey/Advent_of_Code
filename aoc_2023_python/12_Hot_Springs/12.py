def get_records(input_file):
    with open(input_file, "r") as file:
        data = file.readlines()
    records = [
        (
            line.strip().split()[0],
            list(map(int, line.strip().split()[1].split(","))),
        )
        for line in data
    ]
    return records


def get_amount(line):
    row, parts = line
    len_row = len(row)
    len_parts = len(parts)

    def _get_amount(r_i, p_i, part_len):
        def _go_to_dot():
            if part_len == 0:
                return _get_amount(r_i + 1, p_i, 0)
            elif p_i < len_parts and part_len == parts[p_i]:
                return _get_amount(r_i + 1, p_i + 1, 0)
            else:
                return 0

        def _go_to_hash():
            # return _get_amount(r_i + 1, p_i, part_len + 1)
            if p_i < len_parts and part_len < parts[p_i]:
                return _get_amount(r_i + 1, p_i, part_len + 1)
            return 0

        if r_i == len_row:
            if p_i == len_parts and part_len == 0:
                return 1
            elif p_i == len_parts - 1 and part_len == parts[p_i]:
                return 1
            else:
                return 0

        current_spring = row[r_i]
        result = 0
        if current_spring == ".":
            result += _go_to_dot()
        elif current_spring == "#":
            result += _go_to_hash()
        elif current_spring == "?":
            result += _go_to_hash()
            result += _go_to_dot()
        else:
            assert False

        return result

    return _get_amount(0, 0, 0)


def get_answer_1(records):
    return sum(map(get_amount, records))


def main():
    records = get_records("input")
    print(get_answer_1(records))


if __name__ == "__main__":
    assert get_amount(("???.###", [1, 1, 3])) == 1
    assert get_amount((".??..??...?##.", [1, 1, 3])) == 4
    assert get_amount(("?#?#?#?#?#?#?#?", [1, 3, 1, 6])) == 1
    assert get_amount(("????.#...#...", [4, 1, 1])) == 1
    assert get_amount(("????.######..#####.", [1, 6, 5])) == 4
    assert get_amount(("?###????????", [3, 2, 1])) == 10

    main()
