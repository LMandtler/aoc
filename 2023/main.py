import os
import importlib

day = 6
example = False

solution = importlib.import_module(f'solutions.day{day}')
inputfile = 'example' if example else 'input'

with open(os.path.join(os.path.dirname(__file__), 'data', f'day{day}', inputfile)) as f:
    lines = f.readlines()
    solver = solution.solver(lines)
    solver.process_lines()

print(solver.total_part1)
print(solver.total_part2)