import re

def check_matches(value):
  if len(value) == 2 and value[0] == value[1]:
    return True

  for i in range(1, round(len(value) / 2) + 1):
    items = value.split(value[:i])
    unique_items = set(items)
    if len(unique_items) == 1:
      return True
  return False

def get_invalid_values_in_range(start, end):
  sum = 0
  for i in range(int(start), int(end) + 1):
    value = str(i)
    if check_matches(value):
      sum += i
  return sum
  
def main():
  f = open("./q2/q2_input.txt", "r")

  sum = 0
  for line in f:
    num_ranges = line.split(',')
    for num_range in num_ranges:
      [start, end] = num_range.split('-')
    
      sum += get_invalid_values_in_range(start, end)
   
  print(sum)

main()