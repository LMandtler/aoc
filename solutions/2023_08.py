from dataclasses import dataclass
from math import lcm
@dataclass
class node():
    root: str
    left: str
    right: str

    def starting(self):
        return self.root[2] == 'A'
    
    def ending(self):
        return self.root[2] == 'Z'
    
    def get_next(self, lr):
        if lr == 'L':
            return self.left
        elif lr == 'R':
            return self.right

@dataclass
class direction():
    dirlist:list[str]
    index:int = 0

    def get_next(self):
        next_dir = self.dirlist[self.index]
        self.index += 1
        if self.index == len(self.dirlist):
            self.index = 0
        return next_dir

@dataclass
class solver():
    lines: list[str]
    lr = False
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        nodes = {}
        for line in self.lines:
            val = self.process_line(line)
            if self.lr and val:
                nodes[val.root] = val
            elif not self.lr and val:
                directions:direction = val
                self.lr = True
        # part1
        reached = False
        steps1 = 0
        current:node = nodes['AAA']
        while not reached:
            lr = directions.get_next()
            steps1 += 1
            current = nodes[current.get_next(lr)]

            if current.root == 'ZZZ':
                reached = True

        # part2
        reached = False
        steps2 = 0
        currents = [x for x in nodes.values() if x.starting()]
        directions.index = 0
        local_reached = []
        while not reached:
            lr = directions.get_next()
            steps2 += 1

            for i, x in enumerate(currents):
                x = nodes[x.get_next(lr)]
                currents[i] = x
                if x.ending():
                    local_reached.append(steps2)

            if len(local_reached) == len(currents):
                break
                      
        self.total_part1 = steps1
        self.total_part2 = lcm(*local_reached)

    def process_line(self, line):
        line = line.strip()

        if line:
            if not self.lr:
                return direction(line)
            else:
                values = line.split(' = ')
                root = values[0]
                values = values[1].split(', ')
                n = node(root, values[0].replace('(', ''), values[1].replace(')', ''))
                return n
        return None
