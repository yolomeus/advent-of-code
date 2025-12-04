from itertools import product

from utils import read_file_as_tuples


def adjacent_positions(i, j):
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


def main():
    grid = read_file_as_tuples("data/day_04.txt")
    w, h = len(grid[0]), len(grid)

    accessible_rolls = 0
    for i, j in product(range(w), range(h)):
        num_adjacent_rolls = 0

        if grid[i][j] != "@":
            continue

        for x, y in adjacent_positions(i, j):
            if 0 <= x < w and 0 <= y < h:
                if grid[x][y] == "@":
                    num_adjacent_rolls += 1

        if not num_adjacent_rolls > 3:
            accessible_rolls += 1

    print("Part 1:", accessible_rolls)


if __name__ == "__main__":
    main()
