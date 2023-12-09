import os
from aocd import get_data
import importlib
import shutil

year = 2023
day = 9

# check if example file and solution file exist, else create them
if not os.path.exists(f'data/{year}_{str(day).zfill(2)}_example.txt'):
    print("Please provide the example data:")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
        text = '\n'.join(lines)

    with open(f'data/{year}_{str(day).zfill(2)}_example.txt', 'w') as f:
        f.write(text)
if not os.path.exists(f'solutions/{year}_{str(day).zfill(2)}.py'):
    shutil.copy('solutions/template.py', f'solutions/{year}_{str(day).zfill(2)}.py')

solution = importlib.import_module(f'solutions.{year}_{str(day).zfill(2)}')
get_data(day=day, year=year)

for inputfile in [f'data/{year}_{str(day).zfill(2)}_example.txt', os.path.expanduser(f'data/github.LMandtler.1904796/{year}_{str(day).zfill(2)}_input.txt')]:
    with open(inputfile) as f:
        lines = f.readlines()
        solver = solution.solver(lines)
        solver.process_lines()
    print(inputfile)
    print('    ', solver.total_part1)
    print('    ', solver.total_part2)