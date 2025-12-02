from collections.abc import Callable

from utils import read_file


def get_ranges(raw_text: str):
    ranges_raw = raw_text.split(",")
    return [
        range(int(a), int(b) + 1) for a, b in map(lambda x: x.split("-"), ranges_raw)
    ]


def is_valid_part1(id_: str) -> bool:
    if len(id_) % 2 != 0:
        return True

    middle = len(id_) // 2
    a, b = id_[:middle], id_[middle:]
    return a != b


def is_valid_part2(id_: str) -> bool:
    # for at repeating number we need to partition into at least two numbers
    id_middle = len(id_) // 2
    possible_lengths = tuple(range(1, id_middle + 1))

    for length in possible_lengths:
        all_sub_ids_equal = all(
            id_[i : i + length] == id_[:length] for i in range(0, len(id_), length)
        )
        if all_sub_ids_equal:
            return False

    return True


def sum_invalid_ids(ranges: list[range], is_valid: Callable[[str], bool]) -> int:
    invalid_id_sum = 0
    for range_ in ranges:
        for id_ in range_:
            if not is_valid(str(id_)):
                invalid_id_sum += id_

    return invalid_id_sum


def main():
    raw_text = read_file("data/day_02.txt")
    ranges = get_ranges(raw_text)

    print("Part 1:", sum_invalid_ids(ranges, is_valid_part1))
    print("Part 2:", sum_invalid_ids(ranges, is_valid_part2))


if __name__ == "__main__":
    main()
