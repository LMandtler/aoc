import os
from aocd import get_data
import importlib

year = 2023
day = 6

solution = importlib.import_module(f'solutions.{year}_{str(day).zfill(2)}')
get_data(day=day, year=year)

for inputfile in [f'data/{year}_{str(day).zfill(2)}_example.txt', os.path.expanduser(f'~/.config/aocd/github.LMandtler.1904796/{year}_{str(day).zfill(2)}_input.txt')]:
    with open(inputfile) as f:
        lines = f.readlines()
        solver = solution.solver(lines)
        solver.process_lines()
    print(inputfile)
    print('    ', solver.total_part1)
    print('    ', solver.total_part2)