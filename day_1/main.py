#!/usr/bin/env python3
import os
import sys


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


if __name__ == '__main__':
    print(part_1())
