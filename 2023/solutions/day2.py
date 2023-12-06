from dataclasses import dataclass

check = {'red': 12, 'green': 13, 'blue': 14}

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
        values = line.split(':')
        gamenumber = int(values[0].split(' ')[1])
        rounds = values[1].split(';')
        valid = True
        minSet = {'red': 0, 'green': 0, 'blue': 0}
        for round in rounds:
            draws = round.split(',')
            for draw in draws:
                d = draw.strip().split(' ')
                if check[d[1]] < int(d[0]):
                    valid = False
                minSet[d[1]] = max(minSet[d[1]], int(d[0]))
        power = minSet['red'] * minSet['green'] * minSet['blue']
        
        part1 = gamenumber if valid else 0
        part2 = power

        return part1, part2    
