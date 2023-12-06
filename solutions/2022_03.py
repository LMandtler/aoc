from dataclasses import dataclass

@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        lines = []
        for line in self.lines:
            part1, line = self.process_line(line)
            self.total_part1 += part1
            lines.append(line)
            if len(lines) == 3:
                c = set.intersection(lines[0], lines[1], lines[2])
                for item in c:
                    val = ord(item) - 96
                    if val < 0:
                        val = ord(item) - 38
                    self.total_part2 += val
                lines = []

    def process_line(self, line):
        line = line.strip()
        length = int(len(line) / 2)
        a = set([x for x in line[:length]])
        b = set([x for x in line[length:]])
        c = set.intersection(a, b)
        val = 0
        for item in c:
            val = ord(item) - 96
            if val < 0:
                val = ord(item) - 38
        return val, set(line)
