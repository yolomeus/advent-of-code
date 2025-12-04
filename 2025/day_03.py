from collections.abc import Callable
from functools import partial

from utils import read_file_as_lines


def sum_joltages(
    battery_banks: tuple[tuple[int, ...], ...],
    compute_joltage_fn: Callable[[tuple[int, ...]], int],
) -> int:
    total_joltage = 0
    for line in battery_banks:
        total_joltage += compute_joltage_fn(line)

    return total_joltage


def compute_joltage(battery_bank: tuple[int, ...], n_batteries: int) -> int:
    max_joltage = battery_bank[:1]
    rest = battery_bank[1:]
    while rest:
        num, *rest = rest
        while (
            max_joltage
            and num > max_joltage[-1]
            and len(max_joltage) + len(rest) >= n_batteries
        ):
            max_joltage = max_joltage[:-1]

        if len(max_joltage) < n_batteries:
            max_joltage = max_joltage + (num,)

    return int("".join(map(str, max_joltage)))


def main():
    lines = read_file_as_lines("data/day_03.txt")
    battery_banks = tuple(map(lambda x: tuple(map(int, x)), lines))

    print(
        "Part 1:",
        sum_joltages(battery_banks, partial(compute_joltage, n_batteries=2)),
    )
    print(
        "Part 2:",
        sum_joltages(battery_banks, partial(compute_joltage, n_batteries=12)),
    )


if __name__ == "__main__":
    main()
