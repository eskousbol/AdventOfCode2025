def main():
  f = open("./q5/q5_input.txt", "r")

  fresh_ingredient_count = 0
  num_ranges = []
  values = []
  for line in f:
    line = line.strip()
    if len(line) == 0:
      continue

    if len(line.split('-')) == 2:
      num_ranges.append(line.split('-'))
    else:
      values.append(int(line))

  f.close()
  for value in values:
    for [lower_limit, upper_limit] in num_ranges:
      if value >= int(lower_limit) and value <= int(upper_limit):
        fresh_ingredient_count += 1
        break

  print(fresh_ingredient_count)

main()