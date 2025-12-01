from math import floor

from utils import read_file_as_lines


def part1(nums: tuple[int, ...]) -> int:
    zero_count = 0

    dial = 50
    for num in nums:
        dial = (dial + num) % 100

        if dial == 0:
            zero_count += 1

    return zero_count


def part2(nums: tuple[int, ...]) -> int:
    zero_count = 0

    dial = 50
    for num in nums:
        zero_count += floor(abs(num) / 100)
        extra_step = num % -100 if num < 0 else num % 100
        if dial + extra_step < 0 or dial + extra_step > 99:
            zero_count += 1

        dial = (dial + num) % 100

    return zero_count


def main():
    raw_lines = read_file_as_lines("data/day_01.txt")
    nums = tuple(map(lambda x: int(x.replace("L", "-").replace("R", "+")), raw_lines))

    print(f"Part 1: {part1(nums)}")
    print(f"Part 2: {part2(nums)}")


if __name__ == "__main__":
    main()
