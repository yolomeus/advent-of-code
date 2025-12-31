from pathlib import Path

from utils import read_file_as_tuples


def compute_next_line(
    previous_line: tuple[str, ...], splitter_line: tuple[str, ...]
) -> tuple[list, int]:
    assert len(previous_line) == len(splitter_line)

    if "S" in previous_line:
        return tuple(map(lambda x: "|" if x == "S" else x, previous_line)), 0

    n = len(previous_line)
    num_splits = 0
    resulting_line = ["."] * n

    for i in range(n):
        if previous_line[i] == "|" and splitter_line[i] == "^":
            resulting_line[i - 1] = "|"
            resulting_line[i + 1] = "|"
            num_splits += 1
        elif previous_line[i] == "|" and splitter_line[i] == ".":
            resulting_line[i] = "|"

    return resulting_line, num_splits


def main():
    x = read_file_as_tuples(Path("data/day_07.txt"))
    total_splits = 0
    previous_line = x[0]
    for i in range(0, len(x), 2):
        splitter_line = x[i]
        previous_line, num_splits = compute_next_line(previous_line, splitter_line)
        total_splits += num_splits

    print("Part 1:", total_splits)


if __name__ == "__main__":
    main()
