from utils import read_file_as_lines


def part1(battery_bank: tuple[tuple[int, ...], ...]) -> int:
    total_joltage = 0
    for line in battery_bank:
        max_joltage = 0
        for i in range(len(line) - 1):
            for j in range(len(line) - 1, i, -1):
                joltage = int(f"{line[i]}{line[j]}")
                max_joltage = max(max_joltage, joltage)

        total_joltage += max_joltage

    return total_joltage


def main():
    lines = read_file_as_lines("data/day_03.txt")
    battery_bank = tuple(map(lambda x: tuple(map(int, x)), lines))

    print("Part 1:", part1(battery_bank))


if __name__ == "__main__":
    main()
