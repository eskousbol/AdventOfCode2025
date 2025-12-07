def main():
  f = open("./q2/q2_input.txt", "r")

  sum = 0
  for line in f:
    num_ranges = line.split(',')
    for num_range in num_ranges:
      [start, end] = num_range.split('-')
    
      for i in range(int(start), int(end) + 1):
        value = str(i)
        if value[0:round(len(value)/2)] == value[round(len(value)/2):]:
          sum += i
   
  print(sum)
  f.close()

main()