from collections.abc import Callable

from utils import read_file_as_lines


def sum_joltages(
    battery_banks: tuple[tuple[int, ...], ...],
    compute_joltage: Callable[[tuple[int, ...]], int],
) -> int:
    total_joltage = 0
    for line in battery_banks:
        total_joltage += compute_joltage(line)

    return total_joltage


def compute_joltage_part1(battery_bank: tuple[int, ...]):
    max_joltage = 0
    for i in range(len(battery_bank) - 1):
        for j in range(len(battery_bank) - 1, i, -1):
            joltage = int(f"{battery_bank[i]}{battery_bank[j]}")
            max_joltage = max(max_joltage, joltage)
    return max_joltage


def compute_joltage_part2(battery_bank: tuple[int, ...]):
    max_joltage = battery_bank[:1]
    rest = battery_bank[1:]
    while rest:
        num, *rest = rest
        while (
            max_joltage and num > max_joltage[-1] and len(max_joltage) + len(rest) >= 12
        ):
            max_joltage = max_joltage[:-1]

        if len(max_joltage) < 12:
            max_joltage = max_joltage + (num,)

    return int("".join(map(str, max_joltage)))


def main():
    lines = read_file_as_lines("data/day_03.txt")
    battery_banks = tuple(map(lambda x: tuple(map(int, x)), lines))

    print("Part 1:", sum_joltages(battery_banks, compute_joltage_part1))
    print("Part 2:", sum_joltages(battery_banks, compute_joltage_part2))


if __name__ == "__main__":
    main()
