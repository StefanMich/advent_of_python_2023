#!/usr/bin/env python3
from collections import defaultdict
import re


def part_1():
    with open('input') as f:
        lines = f.readlines()
    total_points = 0
    for line in lines:
        winners = score_card(line)
        if winners:
            points = pow(2, (len(winners) - 1))
            total_points += points
    return total_points


def part_2():
    with open('input') as f:
        lines = f.readlines()
    copies = {}

    for i, line in enumerate(lines):
        copies[i] = 1

    for i, line in enumerate(lines):
        winners = score_card(line)
        if winners:
            for x in range(1, len(winners) + 1):
                copies[i + x] += copies[i]
    return sum(copies.values())


def score_card(line):
    card_number, numbers = line.split(':')
    winning, actual = numbers.split('|')
    winning = {w for w in winning.strip().split()}
    actual = {a for a in actual.strip().split()}
    winners = actual.intersection(winning)
    return winners


if __name__ == '__main__':
    print(part_1())
    print(part_2())
