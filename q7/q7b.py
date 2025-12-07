import functools

class Grid:
  def __init__(self, grid):
    self.grid = grid
  
  @functools.cache
  def send_beam(self, position):
    split_count = 0
    
    new_position = [position[0] + 1, position[1]]
    if new_position[0] > len(self.grid) - 1:
      return split_count

    if self.grid[new_position[0]][new_position[1]] == '^':
      split_count += 1
      if  new_position[1] > 0:
        split_count += self.send_beam((new_position[0], new_position[1] - 1))
      if new_position[1] < len(self.grid[new_position[0]]) - 1:
        split_count += self.send_beam((new_position[0], new_position[1] + 1))
    
    else:
      split_count += self.send_beam((new_position[0], new_position[1]))

    return split_count

def main():
  grid = []
  start_position = None
  with open("./q7/q7_input.txt", "r") as f:
    i = 0
    for line in f:
      row = list(line.strip())
      grid.append(row)
      if not start_position and row.index('S') != -1:
        start_position = (i, row.index('S'))

      i += 1
  
  grid = Grid(grid)
  split_count = grid.send_beam(start_position)

  print(split_count + 1)

main()