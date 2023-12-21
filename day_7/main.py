#!/usr/bin/env python3
from collections import Counter
from enum import IntEnum


# lowest to highest
order = '23456789TJQKA'


class Type(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, cards: str):
        self.cards = cards
        self.counter = Counter(self.cards).most_common()

    def type(self) -> Type:
        if self.is_five_of_a_kind():
            return Type.FIVE_OF_A_KIND
        elif self.is_four_of_a_kind():
            return Type.FOUR_OF_A_KIND
        elif self.is_full_house():
            return Type.FULL_HOUSE
        elif self.is_three_of_a_kind():
            return Type.THREE_OF_A_KIND
        elif self.is_two_pair():
            return Type.TWO_PAIR
        elif self.is_one_pair():
            return Type.ONE_PAIR
        else:
            return Type.HIGH_CARD

    def is_five_of_a_kind(self) -> bool:
        _, count = self.counter[0]
        return count == 5

    def is_four_of_a_kind(self) -> bool:
        _, count = self.counter[0]
        return count == 4

    def is_three_of_a_kind(self) -> bool:
        _, count = self.counter[0]
        return count == 3

    def is_full_house(self) -> bool:
        _, top_count = self.counter[0]
        _, second_count = self.counter[1]
        return top_count == 3 and second_count == 2

    def is_two_pair(self) -> bool:
        _, top_count = self.counter[0]
        _, second_count = self.counter[1]
        return top_count == 2 and second_count == 2

    def is_one_pair(self) -> bool:
        _, top_count = self.counter[0]
        return top_count == 2

    def is_high_card(self) -> bool:
        _, top_count = self.counter[0]
        return top_count == 1

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented

        if self.type() == other.type():
            return self.second_order(other)
        return self.type() < other.type()

    def second_order(self, other: object) -> bool:
        if not isinstance(other, Hand):
            return NotImplemented

        comparisons = zip(self.cards, other.cards)
        for comparison in comparisons:
            left, right = comparison
            if left != right:
                return order.index(left) < order.index(right)
        return False


def part_1() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()

    hands: list[tuple[Hand, int]] = list()
    for line in lines:
        _cards, _bid = line.split(' ')
        hands.append((Hand(_cards), int(_bid)))

    hands.sort(key=lambda x: x[0])
    total_winnings = 0
    for i, (cards, bid) in enumerate(hands, start=1):
        total_winnings += i * bid

    return total_winnings


if __name__ == '__main__':
    print(part_1())
