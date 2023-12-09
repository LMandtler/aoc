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
        values = [int(x) for x in line.split()]
        sets = [values]
        
        while True:
            diffs = []
            for i in range(len(values) - 1):
                diffs.append(values[i + 1] - values[i])
            sets.append(diffs)
            if all(diffs == 0 for diffs in sets[-1]):
                break
            else:
                values = sets[-1]
        val1 = 0
        val2 = 0
        sets.reverse()
        for i in sets:
            val1 += i[-1]
            val2 = i[0] - val2
        return val1,val2
