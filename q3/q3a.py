def main():
  f = open("./q3/q3_input.txt", "r")

  sum = 0
  for line in f:
    battery = list(line.strip())
    start_items = set(battery[:-1])
    max_start_item = max(start_items)

    start_index = battery.index(max_start_item)

    end_items = set(battery[start_index + 1:])
    max_end_item = max(end_items)
    sum += int(max_start_item + max_end_item)
   
  print(sum)

main()