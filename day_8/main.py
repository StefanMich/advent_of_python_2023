#!/usr/bin/env python3
from dataclasses import dataclass
import re


@dataclass
class Node:
    element: str
    left: str
    right: str

    def __init__(self, line: str) -> None:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
        self.element, self.left, self.right = match.groups()


def part_1() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()

    instructions = lines.pop(0).strip()
    lines.pop(0)

    nodes: dict[str, Node] = dict()

    for line in lines:
        node = Node(line)
        nodes[node.element] = node

    current = nodes['AAA']
    iterations = 0

    while True:
        for instruction in instructions:
            if instruction == 'L':
                current = nodes[current.left]
            elif instruction == 'R':
                current = nodes[current.right]
            iterations += 1
            if current.element == 'ZZZ':
                return iterations

    return iterations


if __name__ == '__main__':
    print(part_1())
