def merge_ranges(num_ranges):
  merged_ranges = []
  made_merges = False
  for [lower_limit, upper_limit] in num_ranges:
    added_value_via_merge = False
    for i in range(len(merged_ranges)):
      [merged_lower_limit, merged_upper_limit] = merged_ranges[i]
      if lower_limit > merged_upper_limit:
        continue

      made_merges = True
      added_value_via_merge = True
      merged_ranges[i] = [min(lower_limit, merged_lower_limit), max(upper_limit, merged_upper_limit)]
    if not added_value_via_merge:
      merged_ranges.append([lower_limit, upper_limit])

  if made_merges:
    return merge_ranges(merged_ranges)
  
  return merged_ranges

def main():
  f = open("./q5/q5_input.txt", "r")

  fresh_ingredients_count = 0
  num_ranges = []
  for line in f:
    line = line.strip()
    if len(line.split('-')) == 2:
      values = line.split('-')
      num_ranges.append([int(values[0]), int(values[1])])

  num_ranges.sort(key=lambda num_range: num_range[0])
  num_ranges = merge_ranges(num_ranges)
      
  for num_range in num_ranges:
    fresh_ingredients_count += num_range[1] - num_range[0] + 1

  print(fresh_ingredients_count)

main()