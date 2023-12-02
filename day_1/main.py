#!/usr/bin/env python3
from dataclasses import dataclass
import os
import sys
from typing import Optional


def part_1():
    with open('input') as f:
        lines = f.readlines()

    calibration_value = 0

    for line in lines:
        left = ''
        right = ''
        for c in line:
            if c.isdigit():
                left = int(c)
                break

        for c in reversed(line):
            if c.isdigit():
                right = int(c)
                break

        value = 10 * left + right
        calibration_value += value
    return calibration_value

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


@dataclass
class Location:
    index: int
    value: Optional[int] = None


def part_2():

    with open('input') as f:
        lines = f.readlines()

    calibration_value = 0

    for line in lines:

        left = Location(index=sys.maxsize)
        right = Location(index=-1)

        for number_str, number in numbers.items():
            start = 0
            while (index := line.find(number_str, start)) != -1:
                if index < left.index:
                    left.index = index
                    left.value = number
                if index > right.index:
                    right.index = index
                    right.value = number
                start = index + 1

        print(line, left.value, right.value)
        value = 10 * left.value + right.value
        calibration_value += value
    return calibration_value


if __name__ == '__main__':
    print(part_1())
    print(part_2())
