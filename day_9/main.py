#!/usr/bin/env python3
from dataclasses import (
    dataclass,
    field,
)


@dataclass
class Report:
    report_line: list[int]
    differences: list[list[int]] = field(default_factory=list)
    extrapolated_value: int = 0

    def calculate_differences(self) -> None:
        self.differences.insert(0, self.report_line)
        previous_line = self.report_line

        all_zeros = False
        while not all_zeros:
            temp = list()
            for number in zip(previous_line, previous_line[1:]):
                temp.append(number[1] - number[0])
            self.differences.append(temp)
            previous_line = temp
            all_zeros = all(number == 0 for number in temp)

    def extrapolate_values(self) -> None:
        reversed_differences = reversed(self.differences)
        extrapolated_value = 0

        for i, difference in enumerate(reversed_differences):
            if i == 0:
                difference.append(extrapolated_value)
            else:
                extrapolated_value = difference[-1] + extrapolated_value
                difference.append(extrapolated_value)

        self.differences = reversed(list(reversed_differences))
        self.extrapolated_value = extrapolated_value


def part_1() -> int:
    with open('input') as f:
        lines: list[str] = f.readlines()

    report_lines = list()

    for line in lines:
        report_lines.append(list(map(int, line.strip().split())))

    reports = list()

    for report in report_lines:
        report = Report(report)
        report.calculate_differences()
        report.extrapolate_values()
        reports.append(report)

    return sum(report.extrapolated_value for report in reports)


if __name__ == '__main__':
    print(part_1())
