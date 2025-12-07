import re
import math

def main():
  f = open("./q1/q1_input.txt", "r")

  value = 50
  times_hit_zero = 0
  for line in f:
    [(direction, distance)] = re.findall("(L|R)(\\d+)", line)
    distance = int(distance)
    original_value = value
    value += distance % 100 if direction == 'R' else (distance % 100) * -1

    rotations = math.trunc(abs(distance) / 100)
    times_hit_zero += rotations
    
    if value == 0:
      times_hit_zero += 1
    elif original_value == 0 and value < 0:
      value = value % 100
    elif value < 0 or value > 99:
      times_hit_zero += 1
      value = value % 100

  
  print(times_hit_zero)
  f.close()

main()