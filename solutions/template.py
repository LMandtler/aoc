from dataclasses import dataclass

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
        return 0,0
