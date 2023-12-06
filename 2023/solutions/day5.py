from dataclasses import dataclass, field
import sys

@dataclass
class interval():
    start: int
    end: int

@dataclass
class conversion():
    source: int
    target: int
    range: int

    def get_intersection(self, iv: interval):
        min_value = max(self.source, iv.start)
        max_value = min(self.source + self.range, iv.end)

        if min_value <= max_value:
            # check if parts of iv remains not intersected on the smaller or bigger side
            iv_left = interval(iv.start, min_value - 1) if iv.start < min_value else None
            iv_right = interval(max_value + 1, iv.end) if iv.end > max_value else None

            # calculate the target for the matching interval
            iv_matching = interval(self.target + (min_value - self.source), self.target + (max_value - self.source))

            return iv_matching, iv_left, iv_right
        return None



@dataclass
class converter():
    source: str
    target: str
    conversion_map: list[conversion] = field(default_factory=lambda: [])

    def append_conversions(self, conversions: conversion):
        self.conversion_map.append(conversions)

    def get_value(self, value):
        for conversion in self.conversion_map:
            if value >= conversion.source and value < conversion.source + conversion.range:
                i = value - conversion.source
                return conversion.target + i
        return value
    
    def get_value2(self, iv: interval):
        # return the mapped values for the interval. These may be multiple intervals
        for conversion in self.conversion_map:
            intersection = conversion.get_intersection(iv)
            if intersection:
                target_matching, iv_left, iv_right = intersection
                
                target_left = self.get_value2(iv_left) if iv_left else None
                target_right = self.get_value2(iv_right) if iv_right else None
                return [target_matching] + (target_left if target_left else []) + (target_right if target_right else [])
        return [iv]


@dataclass
class solver():
    lines: list[str]
    total_part1: int = sys.maxsize
    total_part2: int = sys.maxsize
    seeds: list[int] = field(default_factory=lambda: [])
    current_converter: converter | None = None
    converters: dict[str, converter] = field(default_factory=lambda: {})

    def process_lines(self):
        for line in self.lines:
            self.process_line(line)
            # self.total_part1 += part1
            # self.total_part2 += part2
        if self.current_converter:
            self.converters[self.current_converter.source] = self.current_converter

        first_value = None
        for seed_value in self.seeds:
            if first_value:
                sources = [interval(first_value, first_value + seed_value)]
                source = 'seed'
                while source in self.converters:
                    targets = []
                    for iv in sources:
                        targets += self.converters[source].get_value2(iv)
                    sources = targets
                    source = self.converters[source].target
                first_value = None
                self.total_part2 = min(min([i.start for i in targets]), self.total_part2)
            else:
                first_value = seed_value

            value = seed_value
            source = 'seed'
            while source in self.converters:
                value = self.converters[source].get_value(value)
                source = self.converters[source].target
            self.total_part1 = min(value, self.total_part1)


    def process_line(self, line):
        if line.startswith('seeds'):
            self.seeds = [int(x) for x in line.split(':')[1].strip().split()]
        elif line == '\n':
            if self.current_converter:
                self.converters[self.current_converter.source] = self.current_converter
            self.current_converter = None
        elif self.current_converter is None:
            source_target = line.strip().split()[0].split('-to-')
            self.current_converter = converter(source_target[0], source_target[1]) 
        else:
            values = [int(x) for x in line.split()]
            c = conversion(values[1], values[0], values[2])
            self.current_converter.append_conversions(c)
