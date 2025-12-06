from collections.abc import Iterable
from functools import reduce

from utils import read_file_as_lines

operations = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}


def part1(homework_lines: Iterable[list[str]]):
    columns = tuple(zip(*homework_lines))
    total = 0
    for col in columns:
        *values, operation_symbol = col
        values = map(int, values)
        total += reduce(operations[operation_symbol], values)

    return total


def main():
    homework_lines = map(str.split, read_file_as_lines("data/day_06.txt"))
    print("Part 1:", part1(homework_lines))


if __name__ == '__main__':
    main()
