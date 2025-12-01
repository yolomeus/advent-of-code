from collections import deque
from itertools import product

from util import read_file

Matrix = tuple[tuple[int, ...], ...]


def in_bounds(y: int, x: int, height: int, width: int) -> bool:
    return (0 <= y < height) and (0 <= x < width)


def get_neighbors(y: int, x: int, height: int, width: int):
    return filter(
        lambda plot: in_bounds(plot[0], plot[1], height, width),
        ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)),
    )


def scan_regions(
    garden_plots: Matrix, height: int, width: int
) -> list[set[tuple[int, int]]]:
    all_plots = list(product(range(height), range(width)))
    regions = []
    while len(all_plots) > 0:
        seed = all_plots.pop()
        y_seed, x_seed = seed
        plant_type = garden_plots[y_seed][x_seed]

        region = {seed}
        neighborhoods_to_check = deque([seed])

        while len(neighborhoods_to_check) > 0:
            cur_plot = neighborhoods_to_check.popleft()
            neighbors = get_neighbors(*cur_plot, height, width)
            # if the neighbor is part of the region, we've already checked it
            neighbors = filter(lambda x: x not in region, neighbors)

            for neighbor in neighbors:
                y_neighbor, x_neighbor = neighbor
                neighbor_plant_type = garden_plots[y_neighbor][x_neighbor]
                if neighbor_plant_type == plant_type:
                    region.add(neighbor)
                    neighborhoods_to_check.append(neighbor)
                    all_plots.remove(neighbor)

        regions.append(region)

    return regions


def perimeter(
    region: set[tuple[int, int]],
    garden_plots: Matrix,
    height: int,
    width: int,
):
    result = 0
    for y, x in region:
        fence_candidates = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        for y_adjacent, x_adjacent in fence_candidates:
            if (
                not in_bounds(y_adjacent, x_adjacent, height, width)
                or garden_plots[y_adjacent][x_adjacent] != garden_plots[y][x]
            ):
                result += 1

    return result


def main():
    garden_plots = tuple(map(tuple, read_file("data/day_12.txt").splitlines()))
    height, width = len(garden_plots), len(garden_plots[0])
    regions = scan_regions(garden_plots, height, width)

    total_price = 0
    for region in regions:
        total_price += len(region) * perimeter(region, garden_plots, height, width)

    print(total_price)


if __name__ == "__main__":
    main()
