from dataclasses import dataclass

mapper1 =  {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}
mapper2 =  {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7
}

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
        line = line.strip()
        return mapper1[line], mapper2[line]
