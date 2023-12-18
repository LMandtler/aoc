from dataclasses import dataclass

@dataclass
class coord():
    x: int
    y: int
    dir_from: str
    color: str
    dir_to: str = ''

    def get_values(self):
        return self.x, self.y, self.dir_from, self.dir_to, self.color

# Define a function to parse the input and return a list of coordinates
def parse_input(lines):
  # Initialize the current position and the list of coordinates
  x = 0
  y = 0
  coords = []
  # Loop through each line of the input
  for line in lines:
    # Split the line by space and get the direction, length and color
    direction, length, color = line.split()
    # Convert the length to an integer
    length = int(length)
    # Loop through the length of the segment
    for i in range(length):
      # Update the current position based on the direction
      if direction == "U":
        y += 1
      elif direction == "D":
        y -= 1
      elif direction == "R":
        x += 1
      elif direction == "L":
        x -= 1
      # Append the current position and color to the list of coordinates
      if i == 0 and coords:
        coords[-1].dir_to = direction
      if not i == length - 1:
        coords.append(coord(x, y, direction, color, direction))
      else:
        coords.append(coord(x, y, direction, color))


  # Return the list of coordinates
  return coords

# Define a function to calculate the number of spaces in the grid that belong to the loop
def count_loop_spaces(coords):
  # Initialize the set of loop spaces and the minimum and maximum coordinates
  loop_spaces = {}
  min_x = min_y = max_x = max_y = 0
  # Loop through the coordinates
  for coord in coords:
    x, y, dir_from, dir_to, color = coord.get_values()
    # Add the coordinate to the set of loop spaces
    loop_spaces[(x, y)] = (dir_from, dir_to)
    # Update the minimum and maximum coordinates
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
  # Return the size of the set of loop spaces and the minimum and maximum coordinates
  return loop_spaces, min_x, min_y, max_x, max_y
# Define a function to calculate the inside area of the loop
def count_inside_area(loop_spaces, min_x, min_y, max_x, max_y):
  # Initialize the inside area and the set of visited spaces
  inside_area = 0
  # Loop through the rows and columns of the grid
  for y in range(max_y, min_y - 1, -1):
    inside_counter = 0
    last_vert_dir = ''
    row = ''
    cr = 0
    
    for x in range(min_x, max_x + 1):
      # auf die loop kommen
      key = (x, y)
      if key in loop_spaces and loop_spaces[key][0] in ['U', 'D']:
        if loop_spaces[key][0] != last_vert_dir:
            last_vert_dir = loop_spaces[key][0]
            inside_counter += 1
      if key in loop_spaces and loop_spaces[key][1] in ['U', 'D']:
        if loop_spaces[key][1] != last_vert_dir:
            last_vert_dir = loop_spaces[key][1]
            inside_counter += 1
        
      if inside_counter % 2 == 1 or key in loop_spaces:
        inside_area += 1
        cr += 1
        row += '#'
      else:
        row += '.'
    with open('grid.txt', 'a') as f:
      f.write(row + f' {cr}' + '\n')

  # Return the inside area
  return inside_area

def print_loop(coords):
  # Initialize the minimum and maximum coordinates
  min_x = min(coords, key=lambda c: c[0])[0]
  min_y = min(coords, key=lambda c: c[1])[1]
  max_x = max(coords, key=lambda c: c[0])[0]
  max_y = max(coords, key=lambda c: c[1])[1]
  # Loop through the rows and columns of the grid
  for y in range(max_y, min_y - 1, -1):
    # Initialize an empty row
    row = ""
    for x in range(min_x, max_x + 1):
      # Check if the coordinate is part of the loop
      if (x, y) in coords:
        # Get the color of the coordinate
        # Append the color to the row
        row += "#"
      else:
        # Append a blank space to the row
        row += "."
    # Print the row
    with open('grid_loop.txt', 'a') as f:
      f.write(row + '\n')

@dataclass
class solver():
    lines: list[str]
    total_part1: int = 0
    total_part2: int = 0

    def process_lines(self):
        # for line in self.lines:
        #     part1, part2 = self.process_line(line)
        #     self.total_part1 += part1
        #     self.total_part2 += part2

        # Parse the input and get the list of coordinates
        coords = parse_input(self.lines)

        # Calculate the number of spaces in the grid that belong to the loop
        loop_spaces, min_x, min_y, max_x, max_y = count_loop_spaces(coords)

        # Calculate the inside area of the loop
        inside_area = count_inside_area(loop_spaces, min_x, min_y, max_x, max_y)

        # Print the results
        print(f"The number of spaces in the grid that belong to the loop is {len(loop_spaces)}.")
        print(f"The inside area of the loop is {inside_area}.")
        self.total_part1 = inside_area
        print_loop(loop_spaces)


    def process_line(self, line):
        return 0,0
