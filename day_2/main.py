#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    blue: int = 0
    red: int = 0
    green: int = 0

    def power(self):
        return self.blue * self.red * self.green


def part_1():
    games = find_min_cubes()
    possible = filter(
        lambda x: x.red <= 12 and x.green <= 13 and x.blue <= 14, games)
    return sum(map(lambda x: x.id, possible))


def part_2():
    games = find_min_cubes()
    sum_of_powers = sum(g.power() for g in games)
    return sum_of_powers

def find_min_cubes():
    with open('input') as f:
        lines = f.readlines()
    games = []
    for line in lines:
        id_line, reveals = line.split(':')
        _, _id = id_line.split(' ')
        game = Game(int(_id))
        games.append(game)
        for reveal in reveals.split(';'):
            color_counts = reveal.split(',')
            for color_count in color_counts:
                count, color = color_count.strip().split(' ')
                current_count = getattr(game, color)
                if int(count) > current_count:
                    setattr(game, color, int(count))
    return games


if __name__ == '__main__':
    print(part_1())
    print(part_2())
