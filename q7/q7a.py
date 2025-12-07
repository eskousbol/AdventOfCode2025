def send_beam(grid, position):
  split_count = 0
  new_position = [position[0] + 1, position[1]]
  if new_position[0] > len(grid) - 1:
    return split_count

  if grid[new_position[0]][new_position[1]] == '|':
    return split_count
  elif grid[new_position[0]][new_position[1]] == '^':
    split_count += 1
    if  new_position[1] > 0:
      split_count += send_beam(grid, [new_position[0], new_position[1] - 1])
    if new_position[1] < len(grid[new_position[0]]) - 1:
      split_count += send_beam(grid, [new_position[0], new_position[1] + 1])
  
  else:
    grid[new_position[0]][new_position[1]] = '|'
    split_count += send_beam(grid, [new_position[0], new_position[1]])

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
        start_position = [i, row.index('S')]

      i += 1
  
  split_count = send_beam(grid, start_position)

  print(split_count)

main()