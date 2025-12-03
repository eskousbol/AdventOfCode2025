def get_largest_next_number(start_index, end_index):
  pass

def main():
  f = open("./q3/q3_input.txt", "r")

  sum = 0
  for line in f:
    battery = list(line.strip())

    remaining_numbers = 12
    final_value = ''
    start_index = -1
    while remaining_numbers > 0:
      battery_subset = battery[start_index + 1:len(battery) - remaining_numbers + 1]
      items = set(battery_subset)
      max_item = max(items)
      start_index = battery_subset.index(max_item) + start_index + 1
      final_value += max_item
      remaining_numbers -= 1

    sum += int(final_value)
   
  print(sum)

main()