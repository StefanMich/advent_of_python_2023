#!/usr/bin/env python3
from functools import reduce
from itertools import zip_longest
from math import (
    ceil,
    floor,
    prod,
)


def part_1() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()

    times = map(int, lines.pop(0).strip().split(':')[1].split())
    distances = map(int, lines.pop(0).strip().split(':')[1].split())

    races = zip(times, distances)

    ways_to_win = calculate_ways_to_win(races)

    ways_to_win_product = prod(ways_to_win.values())
    return ways_to_win_product


def part_2() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()

    times = int(lines.pop(0).strip().split(':')[1].replace(' ', ''))
    distances = int(lines.pop(0).strip().split(':')[1].replace(' ', ''))
    races = [(times, distances)]

    ways_to_win = calculate_ways_to_win(races)[0]

    return ways_to_win


def calculate_ways_to_win(races):
    ways_to_win = dict()
    for i, (time, distance) in enumerate(races):
        # plot as a function of time holding the button, moving the y-axis
        # down by the distance, then finding the x-interceptions.
        # y = (t - h) * h - d = -h² + th - d
        discriminant = time ** 2 - 4 * distance

        root_1 = (-time + discriminant ** 0.5) / -2
        root_2 = (-time - discriminant ** 0.5) / -2

        ways_to_win[i] = floor(root_2) - ceil(root_1) + 1
    return ways_to_win


if __name__ == '__main__':
    print(part_1())
    print(part_2())
