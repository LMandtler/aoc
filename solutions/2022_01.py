from dataclasses import dataclass, field

@dataclass
class ordered():
    values: list[int] = field(default_factory=lambda: [])
    min_value: int = 0

    def add_value(self, value):
        if value > self.min_value:
            self.values.append(value)
            self.values.remove(self.min_value) if len(self.values) > 3 else None
            self.min_value = min(self.values)



@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        subtotal = 0
        o = ordered()
        for line in self.lines:
            value = self.process_line(line)
            if value:
                subtotal += value
            else:
                if subtotal > self.total_part1:
                    self.total_part1 = subtotal
                o.add_value(subtotal)
                subtotal = 0
            if subtotal > self.total_part1:
                self.total_part1 = subtotal
        o.add_value(subtotal)

        self.total_part2 = sum(o.values)
        print(o.values)

    def process_line(self, line):
        line = line.strip()
        if line:
            return int(line)
        else:
            return 0
