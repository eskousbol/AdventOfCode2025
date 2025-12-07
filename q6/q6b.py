def main():
  f = open("./q6/q6_input.txt", "r")

  problem_matrix = []
  value = 0
  for line in f:
    problem_matrix.append(list(line))

  problem_boundaries = []
  for j in range(len(problem_matrix[0])):
    if problem_matrix[0][j] == ' ':
      for i in range(1, len(problem_matrix)):
        if problem_matrix[i][j] != ' ':
          break
      else:
        problem_boundaries.append(j)

  problem_boundaries.append(len(problem_matrix[0]) - 1)

  previous_problem_boundary = 0
  for problem_boundary in problem_boundaries:
    operation = ''.join(problem_matrix[-1][previous_problem_boundary:problem_boundary]).strip()

    problem_output = 0 if operation == '+' else 1

    problem_submatrix = []
    for i in range(len(problem_matrix) - 1):
      problem_submatrix.append(list(problem_matrix[i][previous_problem_boundary:problem_boundary]))
    
    for j in range(len(problem_submatrix[0])):
      sub_value = ''
      for i in range(len(problem_submatrix)):
        sub_value += problem_submatrix[i][j]
      if len(sub_value.strip()) != 0:
        sub_value = int(sub_value.strip()) 
        if operation == '+':
          problem_output += sub_value
        else:
          problem_output *= sub_value
    value += problem_output
    previous_problem_boundary = problem_boundary

  print(value)

main()