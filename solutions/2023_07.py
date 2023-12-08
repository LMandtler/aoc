from dataclasses import dataclass, field
from collections import Counter

mapper1 = {
    'A': 'A',
    'K': 'B',
    'Q': 'C',
    'J': 'D',
    'T': 'E',
    '9': 'F',
    '8': 'G',
    '7': 'H',
    '6': 'I',
    '5': 'J',
    '4': 'K',
    '3': 'L',
    '2': 'M'
}
mapper2 = {
    'A': 'A',
    'K': 'B',
    'Q': 'C',
    'T': 'D',
    '9': 'E',
    '8': 'F',
    '7': 'G',
    '6': 'H',
    '5': 'I',
    '4': 'J',
    '3': 'K',
    '2': 'L',
    'J': 'M',
}

@dataclass
class hand():
    value: int
    cards1: list[str] = field(default_factory=lambda: [])
    cards2: list[str] = field(default_factory=lambda: [])

    def hand_value1(self):
        c = Counter(self.cards1).most_common()
        
        if c[0][1] == 5:
            return 'A' + ''.join(self.cards1)
        if c[0][1] == 4:
            return 'B' + ''.join(self.cards1)
        if c[0][1] == 3 and c[1][1] == 2:
            return 'C' + ''.join(self.cards1)
        if c[0][1] == 3:
             return 'D' + ''.join(self.cards1)
        if c[0][1] == 2 and c[1][1] == 2:
             return 'E' + ''.join(self.cards1)
        if c[0][1] == 2:
             return 'F' + ''.join(self.cards1)

        return 'G' + ''.join(self.cards1)
    def hand_value2(self):
        counter = Counter(self.cards2)
        c = counter.most_common()
        cards = []
        if c[0][0] != 'M':
            cards = [x for x in ''.join(self.cards2).replace('M', c[0][0])]
        elif c[0][1] == 5 and c[0][0] == 'M':
            cards = [x for x in ''.join(self.cards2).replace('M', 'A')]
        else:
            cards = [x for x in ''.join(self.cards2).replace('M', c[1][0])]
        counter = Counter(cards)
        c = counter.most_common()

        if c[0][1] == 5:
            return 'A' + ''.join(self.cards2)
        if c[0][1] == 4:
            return 'B' + ''.join(self.cards2)
        if c[0][1] == 3 and c[1][1] == 2:
            return 'C' + ''.join(self.cards2)
        if c[0][1] == 3:
             return 'D' + ''.join(self.cards2)
        if c[0][1] == 2 and c[1][1] == 2:
             return 'E' + ''.join(self.cards2)
        if c[0][1] == 2:
             return 'F' + ''.join(self.cards2)

        return 'G' + ''.join(self.cards2)
    
@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        hands: list[hand] = []
        for line in self.lines:
            h = self.process_line(line)
            hands.append(h)
            
        hands.sort(key=lambda x: x.hand_value1(), reverse=True)
        self.total_part1 = sum((i+1) * int(x.value) for i, x in enumerate(hands))
        hands.sort(key=lambda x: x.hand_value2(), reverse=True)
        self.total_part2 = sum((i+1) * int(x.value) for i, x in enumerate(hands))

    def process_line(self, line):
        parts = line.strip().split()
        return hand(int(parts[1]), [mapper1[x] for x in parts[0]], [mapper2[x] for x in parts[0]])
