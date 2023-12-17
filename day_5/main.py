#!/usr/bin/env python3


class Range:
    def __init__(self, destination: int, source: int, range: int) -> None:
        self.destination: int = destination
        self.source: int = source
        self.range: int = range

    def __repr__(self) -> str:
        return f'Range({self.destination} {self.source} {self.range})'


class RangedMap:
    def __init__(self) -> None:
        self.ranges: list[Range] = list()

    def __getitem__(self, item: int) -> int:
        for r in self.ranges:
            if item > r.source:
                if item <= r.source + r.range:
                    return r.destination + (item - r.source)
        return item

    def add(self, range: Range) -> None:
        self.ranges.append(range)
        self.ranges.sort(key=lambda x: x.source)


def part_1() -> int:
    with open('input') as f:
        lines = f.readlines()
    seeds = lines.pop(0)
    _, seed_numbers_string = seeds.split(':')
    seed_numbers: list[int] = list(map(int, seed_numbers_string.strip().split(' ')))

    lines.pop(0)

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

    locations = list()
    for seed in seed_numbers:
        result = seed
        for _map in maps:
            result = _map[result]
        locations.append(result)
    return min(locations)


if __name__ == '__main__':
    print(part_1())
