def remove_paper_rolls(grid):
  removed_rolls = 0
  new_grid = []

  for i in range(0, len(grid)):
    row = grid[i]
    new_row = []
    for j in range(0, len(row)):
      item = row[j]
      if item == '.':
        new_row.append('.')
        continue

      adjacent_items = []
      leftmost_index = max(j-1, 0)
      rightmost_index = min(j+1, len(row) - 1) + 1
      if i > 0:
        adjacent_items.extend(grid[i - 1][leftmost_index:rightmost_index])
      
      if j > 0:
        adjacent_items.append(grid[i][leftmost_index])
        
      if j < len(row) - 1:
          adjacent_items.append(grid[i][rightmost_index - 1])

      if i < len(grid) - 1:
        adjacent_items.extend(grid[i + 1][leftmost_index:rightmost_index])

      if adjacent_items.count('@') < 4:
        removed_rolls += 1 
        new_row.append('.')
      else:
        new_row.append('@')
    new_grid.append(new_row)

  return new_grid, removed_rolls

def main():
  f = open("./q4/q4_input.txt", "r")

  grid = []
  for line in f:
    grid.append(list(line.strip()))

  total_rolls_removed = 0
  done = False
  while not done:
    grid, rolls_removed = remove_paper_rolls(grid)

    total_rolls_removed += rolls_removed
    if rolls_removed == 0:
      done = True
      
  print(total_rolls_removed)

main()