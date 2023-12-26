#!/usr/bin/env python3
from dataclasses import dataclass
from math import lcm
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
    instructions, nodes = parse_input()

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


def part_2() -> int:
    instructions, nodes = parse_input()

    start_keys = [key for key in nodes.keys() if key.endswith('A')]
    start_nodes = [nodes[key] for key in start_keys]

    node_iterations = dict()

    for node in start_nodes:
        current_node = node
        iterations = 0
        result = None
        while not result:
            for instruction in instructions:
                if instruction == 'L':
                    current_node = nodes[current_node.left]
                elif instruction == 'R':
                    current_node = nodes[current_node.right]
                iterations += 1
                if current_node.element.endswith('Z'):
                    node_iterations[current_node.element] = iterations
                    result = iterations

    return lcm(*node_iterations.values())


def parse_input():
    with open('input') as f:
        lines: list[str] = f.readlines()
    instructions = lines.pop(0).strip()
    lines.pop(0)
    nodes: dict[str, Node] = dict()
    for line in lines:
        node = Node(line)
        nodes[node.element] = node
    return instructions, nodes


if __name__ == '__main__':
    #print(part_1())
    print(part_2())
