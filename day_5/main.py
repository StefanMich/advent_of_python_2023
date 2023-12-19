#!/usr/bin/env python3
from itertools import zip_longest


class Range:
    def __init__(self, destination: int, source: int, range: int) -> None:
        self.destination: int = destination
        self.source: int = source
        self.range: int = range

    def __repr__(self) -> str:
        return f'Range({self.destination} {self.source} {self.range})'


class RangedMap:
    def __init__(self) -> None:
        self.ranges: list[Range] = [Range(0, 0, 0)]

    def __getitem__(self, item: int) -> int:
        range_with_next = zip_longest(self.ranges, self.ranges[1:])
        # manger range der starter fra 0
        for range, next_range in range_with_next:
            if next_range is None or range.source <= item < next_range.source:
                if item <= range.source + range.range:
                    return range.destination + (item - range.source)
                else:
                    return item
        return item

    def add(self, range: Range) -> None:
        if range.source == 0:
            self.ranges.pop(0)
        self.ranges.append(range)
        self.ranges.sort(key=lambda x: x.source)


def get_seed_numbers(lines: list[str]) -> list[int]:
    seeds = lines.pop(0)
    _, seed_numbers_string = seeds.split(':')
    seed_numbers: list[int] = list(map(int, seed_numbers_string.strip().split(' ')))
    lines.pop(0)
    return seed_numbers


def build_maps(lines: list[str]) -> list[RangedMap]:
    maps = list()
    _map = RangedMap()
    maps.append(_map)
    for line in lines:
        if ':' in line:
            continue
        if line == '\n':
            _map = RangedMap()
            maps.append(_map)
            continue

        destination, source, range = tuple(map(int, line.strip().split(' ')))
        _map.add(Range(destination, source, range))
    return maps


def part_1() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()
    seed_numbers = get_seed_numbers(lines)

    maps = build_maps(lines)

    locations = list()
    for seed in seed_numbers:
        result = seed
        for _map in maps:
            result = _map[result]
        locations.append(result)
    return min(locations)


def part_2() -> int:
    with open('input') as f:
        lines = f.readlines()
    seed_numbers: list[int] = get_seed_numbers(lines)

    maps = build_maps(lines)

    seed_ranges: list[tuple[int, int]] = []
    while seed_numbers:
        start, _range = seed_numbers[:2]
        seed_numbers = seed_numbers[2:]
        seed_ranges.append((start, _range))

    locations = list()

    for start, _range in seed_ranges:
        print(f'starting range from {start} to {start + _range}')
        seed_number = start
        range_end = start + _range
        while seed_number < range_end:
            result = seed_number
            for _map in maps:
                result = _map[result]
            locations.append(result)
            seed_number += 1
    return min(locations)


if __name__ == '__main__':
    #print(part_1())
    print(part_2())
