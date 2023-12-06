import re
from dataclasses import dataclass

letterdigits = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
    'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

def replace_digit_strings(line: str) -> str:
    for i in range(len(line)):
        for key, value in letterdigits.items():
            if line[i:].startswith(key):
                line, _ = re.subn(key, value, line, 1)
                return replace_digit_strings(line)
    return line

@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        for line in self.lines:
            part1, part2 = self.process_line(line)
            self.total_part1 += part1
            self.total_part2 += part2

    def process_line(self, line):
        line2 = replace_digit_strings(line)
        
        # part 1
        digits = re.sub('\D', '', line)
        first = int(digits[0]) * 10
        last = int(digits[-1])
        part1 = first + last
        # part 2
        digits = re.sub('\D', '', line2)
        first = int(digits[0]) * 10
        last = int(digits[-1])
        part2 = first + last

        return part1, part2
