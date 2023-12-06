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
        line = line.strip()
        a, b = line.split(',')
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        
        r = 1 if a1 <= b1 <= b2 <= a2 or b1 <= a1 <= a2 <= b2 else 0
        s = 1 if a1 <= b2 and b1 <= a2 or b1 <= a2 and a1 <= b2 else 0

        return r, s
