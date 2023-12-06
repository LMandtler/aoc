from dataclasses import dataclass
import sys
import math

@dataclass
class race():
    length: int
    max_distance: int
    min_button_push: int = sys.maxsize
    max_button_push: int = 0

    def calc_button_push(self, button_push, change = -1):
        if change == -1:
            change = math.ceil(button_push / 2)
        if button_push >= self.min_button_push:
            print('end', button_push)
            button_push = self.length - self.min_button_push
            distance = (self.length - button_push) * button_push
            if distance > self.max_distance:
                # check one more possibility
                button_push += 1
                distance = (self.length - button_push) * button_push
                self.max_button_push = button_push if distance > self.max_distance else button_push - 1
            else:
                self.max_button_push = button_push - 1
            return
        distance = (self.length - button_push) * button_push
        if distance > self.max_distance:
            self.min_button_push = button_push
            self.calc_button_push(button_push - change, max(1, math.floor(change / 2)))
        else:
            self.calc_button_push(button_push + change, max(1, math.floor(change / 2)))


@dataclass
class solver():
    lines: list[str]
    total_part1: int = 1
    total_part2: int = 0

    def process_lines(self):
        times = []
        distances = []
        for line in self.lines:
            if times:
                distances = self.process_line(line)
            else: 
                times = self.process_line(line)
        
        for i in range(len(times)):
            r = race(int(times[i]), int(distances[i]))
            r.calc_button_push(math.ceil(r.length / 2))
            part1 = r.max_button_push - r.min_button_push + 1
            self.total_part1 *= part1

        # part2
        r = race(int(''.join(times)), int(''.join(distances)))
        r.calc_button_push(math.ceil(r.length / 2))
        self.total_part2 = r.max_button_push - r.min_button_push + 1
        # self.total_part2 += part2

    def process_line(self, line):
        values = line.split()[1:]        
        return values
