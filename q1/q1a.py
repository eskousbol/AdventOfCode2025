import re

def main():
   f = open("./q1/q1_input.txt", "r")

   value = 50
   times_hit_zero = 0
   for line in f:
      [(direction, distance)] = re.findall("(L|R)(\\d+)", line)
      distance = int(distance)
      distance = distance if direction == 'R' else distance * -1
      value += distance

      truncated_value = value % 100
      value = truncated_value

      if value == 0:
         times_hit_zero += 1
   
   print(times_hit_zero)

main()