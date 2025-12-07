def main():
  f = open("./q4/q4_input.txt", "r")

  sum = 0
  grid = []
  for line in f:
    grid.append(list(line.strip()))
  f.close()

  for i in range(0, len(grid)):
    row = grid[i]
    for j in range(0, len(row)):
      item = row[j]
      if item == '.':
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

      sum += 1 if adjacent_items.count('@') < 4 else 0
      
  print(sum)

main()