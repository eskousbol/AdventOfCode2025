import re

def main():
  f = open("./q6/q6_input.txt", "r")

  problem_matrix = []
  value = 0
  for line in f:
    line_values = re.findall("(\\d+|\\+|\\*)", line)
    problem_matrix.append(line_values)

  for j in range(len(problem_matrix[0])):
    operation = problem_matrix[-1][j]

    problem_output = 0 if operation == '+' else 1

    for i in range(len(problem_matrix) - 1):
      if operation == '+':
        problem_output += int(problem_matrix[i][j])
      else:
        problem_output *= int(problem_matrix[i][j])
    value += problem_output
  print(value)

main()