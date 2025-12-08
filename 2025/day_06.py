from collections.abc import Iterable
from functools import reduce

from utils import read_file_as_lines

operations = {
    "*": lambda a, b: a * b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}


def part1(homework_lines: Iterable[list[str]]):
    columns = tuple(zip(*homework_lines))
    total = 0
    for col in columns:
        *values, operation_symbol = col
        values = map(int, values)
        total += reduce(operations[operation_symbol], values)

    return total


def _rpad(line: list[str], length: int) -> list[str]:
    return line + [" "] * (length - len(line))


def part2(homework_lines_raw: tuple[str, ...]) -> int:
    homework_lines = list(map(lambda x: list(x.replace("\n", " ")), homework_lines_raw))

    # make sure all lines have the same length
    max_len = max(len(line) for line in homework_lines)
    *homework_lines, op_symbols = [
        list(reversed(_rpad(line, max_len))) for line in homework_lines
    ]

    total = 0
    current_operands = []
    j = 0
    while j < len(homework_lines[0]):
        current_operand = ""
        for i in range(len(homework_lines)):
            current_symbol = homework_lines[i][j]
            if current_symbol.isdigit():
                current_operand += current_symbol

        if current_operand:
            current_operands.append(int(current_operand))

        if op_symbols[j] != " ":
            total += reduce(operations[op_symbols[j]], current_operands)
            current_operands = []

        j += 1

    return total


def main():
    homework_lines_parsed = list(map(str.split, read_file_as_lines("data/day_06.txt")))
    print("Part 1:", part1(homework_lines_parsed))

    homework_lines_raw = read_file_as_lines("data/day_06.txt", strip_lines=False)
    print("Part 2:", part2(homework_lines_raw))


if __name__ == "__main__":
    main()
