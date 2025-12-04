from itertools import product
from typing import MutableSequence, Sequence

from utils import read_file_as_tuples


def adjacent_positions(i: int, j: int) -> tuple[tuple[int, int], ...]:
    return (
        (i - 1, j - 1),
        (i + 1, j + 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
    )


def is_accessible(grid: Sequence[Sequence[str]], i: int, j: int) -> bool:
    w, h = len(grid[0]), len(grid)
    num_adjacent_rolls = 0
    for x, y in adjacent_positions(i, j):
        if 0 <= x < w and 0 <= y < h:
            if grid[x][y] == "@":
                num_adjacent_rolls += 1
            if num_adjacent_rolls > 3:
                return False

    return True


def part1(grid: Sequence[Sequence[str]]):
    w, h = len(grid[0]), len(grid)

    accessible_rolls = 0
    for i, j in product(range(w), range(h)):
        if grid[i][j] != "@":
            continue
        if is_accessible(grid, i, j):
            accessible_rolls += 1

    return accessible_rolls


def part2(grid: MutableSequence[MutableSequence[str]]):
    w, h = len(grid[0]), len(grid)
    accessible_rolls = 0
    removed_roll = True

    while removed_roll:
        removed_roll = False
        for i, j in product(range(w), range(h)):
            if grid[i][j] != "@":
                continue
            elif is_accessible(grid, i, j):
                grid[i][j] = "."
                accessible_rolls += 1
                removed_roll = True

    return accessible_rolls


def main():
    grid = read_file_as_tuples("data/day_04.txt")
    print("Part 1:", part1(grid))

    mutable_grid = list(map(list, grid))
    print("Part 2:", part2(mutable_grid))


if __name__ == "__main__":
    main()
