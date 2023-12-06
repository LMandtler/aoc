from dataclasses import dataclass, field

@dataclass
class solver():
    lines: list[str]
    dict_cards: dict[int, list[int]] = field(default_factory=lambda: {})
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        max_card = len(self.lines)
        for line in self.lines:
            self.total_part1 += self.process_line(line)
            
        for card_number in self.dict_cards:
            for i in range(card_number + 1, min(card_number + 1 + self.dict_cards[card_number][0], max_card + 1)):
                self.dict_cards[i][1] += self.dict_cards[card_number][1]
            self.total_part2 += self.dict_cards[card_number][1]
    
    def process_line(self, line):
        values = line.split('|')
        card_number = int(values[0].split(':')[0].strip().split()[1])
        winning = set([int(x) for x in values[0].split(':')[1].strip().split()])
        drawn = [int(x) for x in values[1].strip().split()]
        if len(drawn) != len(set(drawn)):
            print('WARNING', values[0].split(':')[0])
        no_matches = len(set.intersection(winning, drawn))
        self.dict_cards[card_number] = [no_matches, 1]

        return 2**(no_matches - 1) if no_matches > 0 else 0