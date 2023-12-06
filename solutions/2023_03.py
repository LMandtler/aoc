import os
from dataclasses import dataclass, field
import re


@dataclass
class number_class:
    position_start: int
    position_end: int
    value: int
    positions = set()
    valid: bool = False
    
    def __post_init__(self):
        self.positions = set(range(self.position_start, self.position_end))
@dataclass
class symbol_class:
    position: int
    value: str
    values: list[int] = field(default_factory=lambda: [])

    def gear_ratio(self):
        if self.value == '*' and len(self.values) == 2:
            return self.values[0] * self.values[1]
        else:
            return 0

    def __repr__(self) -> str:
        return str(self.value)

from dataclasses import dataclass

@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0
    numbers_last = []
    symbols_last = []

    def process_lines(self):
        
        for line in self.lines:
            part1, part2 = self.process_line(line)
            self.total_part1 += part1
            self.total_part2 += part2

    def process_line(self, line):
        line = line.strip()
        number_line = re.sub('\D', '.', line)
        values = number_line.split('.')
        numbers_current = []
        for value in values:
            # check if value is an int
            try:
                value = int(value)
                # find position of value in line
                position = line.find(str(value))
                # create number
                n = number_class(position_start = max(position - 1, 0), position_end = position + len(str(value)) + 1, value = value)
                numbers_current.append(n)
                line = line.replace(str(value), '.' * len(str(value)), 1)
            except:
                pass
        # get all indices in line which are not '.'
        symbols_current = [symbol_class(i, x) for i, x in enumerate(line) if x != '.']

        part1 = 0
        for i in self.numbers_last:
            # intersection between i and indices
            intersection = set.intersection(i.positions, [s.position for s in symbols_current])

            if intersection:
                part1 += i.value
                for s in symbols_current:
                    if s.position in intersection:
                        s.values.append(i.value)
                i.valid = True
        for i in numbers_current:
            # intersection between i and indices
            intersection = set.intersection(i.positions, [s.position for s in symbols_current])
            if intersection:
                part1 += i.value if i.valid != True else 0
                for s in symbols_current:
                    if s.position in intersection:
                        s.values.append(i.value)
                i.valid = True
            intersection = set.intersection(i.positions, [s.position for s in self.symbols_last])
            if intersection:
                part1 += i.value if i.valid != True else 0
                for s in self.symbols_last:
                    if s.position in intersection:
                        s.values.append(i.value)
                i.valid = True         

        self.numbers_last = [n for n in numbers_current if n.valid == False]
        part2 = 0
        for s in self.symbols_last:
            part2 += s.gear_ratio()
        self.symbols_last = symbols_current
        return part1, part2