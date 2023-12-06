#!/usr/bin/env python3
import re


def part_1():
    with open('input') as f:
        lines = f.readlines()
    total_points = 0
    for line in lines:
        card_number, numbers = line.split(':')
        winning, actual = numbers.split('|')
        winning = {w for w in winning.strip().split()}
        actual = {a for a in actual.strip().split()}
        winners = actual.intersection(winning)
        if winners:
            points = pow(2, (len(winners) - 1))
            total_points += points
    return total_points


if __name__ == '__main__':
    print(part_1())
