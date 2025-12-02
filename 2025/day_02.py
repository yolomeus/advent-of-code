from utils import read_file


def get_ranges(raw_text: str):
    ranges_raw = raw_text.split(",")
    return [
        range(int(a), int(b) + 1) for a, b in map(lambda x: x.split("-"), ranges_raw)
    ]


def is_valid_id(id_: int) -> bool:
    id_ = str(id_)

    if len(id_) % 2 != 0:
        return True

    middle = len(id_) // 2
    a, b = id_[:middle], id_[middle:]
    return a != b


def part1(ranges: list[range]) -> int:
    invalid_id_sum = 0
    for range_ in ranges:
        for id_ in range_:
            if not is_valid_id(id_):
                invalid_id_sum += id_

    return invalid_id_sum


def main():
    raw_text = read_file("data/day_02.txt")
    ranges = get_ranges(raw_text)

    print("Part 1:", part1(ranges))


if __name__ == "__main__":
    main()
