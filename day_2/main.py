#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    blue: int = 0
    red: int = 0
    green: int = 0


def part_1():
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
    possible = filter(
        lambda x: x.red <= 12 and x.green <= 13 and x.blue <= 14, games)
    return sum(map(lambda x: x.id, possible))

if __name__ == '__main__':
    print(part_1())
