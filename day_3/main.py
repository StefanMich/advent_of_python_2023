#!/usr/bin/env python3
import re


def part_1():
    with open('input') as f:
        lines = f.readlines()
    parts = []
    for i, line in enumerate(lines):

        matches = re.finditer(r'\d+', line)
        for match in matches:

            start, end = match.span()

            for adjacent_line_index in range(i - 1, i + 2):
                if adjacent_line_index == -1:
                    continue
                try:
                    adjacent_line = lines[adjacent_line_index]
                    adjacent_line = adjacent_line.strip()
                except IndexError:
                    pass
                else:
                    adjusted_start = max(start - 1, 0)
                    adjusted_end = end + 1
                    if any(is_symbol(c) for c in adjacent_line[adjusted_start:adjusted_end]):
                        parts.append(int(match.group()))

                        break
    print(parts)
    return sum(parts)


def is_symbol(c: str):
    dot = c == '.'
    alphanumeric = c.isalnum()
    return not dot and not alphanumeric


if __name__ == '__main__':
    print(part_1())
