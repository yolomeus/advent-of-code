from utils import read_file


def part1(
    ingredient_ids: tuple[int, ...], range_pairs: tuple[tuple[int, ...], ...]
) -> int:
    ranges = [range(start, end + 1) for start, end in range_pairs]
    num_fresh_ingredients = 0
    for id_ in ingredient_ids:
        for r in ranges:
            if id_ in r:
                num_fresh_ingredients += 1
                break

    return num_fresh_ingredients


def part2(range_pairs: tuple[tuple[int, ...], ...]) -> int:
    range_pairs_asc = sorted(range_pairs, key=lambda x: x[0])

    new_ranges = [range_pairs_asc[0]]
    for c, d in range_pairs_asc[1:]:
        a, b = new_ranges[-1]
        if a <= c <= d <= b:
            continue
        elif c <= b:
            new_ranges = new_ranges[:-1] + [(a, d)]
        elif c > b:
            new_ranges += [(c, d)]

    return sum([b - a + 1 for a, b in new_ranges])


def main():
    raw_text = read_file("data/day_05.txt")
    raw_ranges, raw_items = raw_text.split("\n\n")

    ingredient_ids = tuple(map(int, raw_items.split("\n")))
    range_pairs = tuple(
        map(lambda x: tuple(map(int, x.split("-"))), raw_ranges.split("\n"))
    )

    print("Part 1:", part1(ingredient_ids, range_pairs))
    print("Part 2:", part2(range_pairs))


if __name__ == "__main__":
    main()
