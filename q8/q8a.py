import math

def straight_line_distance(box1, box2):
  pos1 = box1.split(',')
  pos2 = box2.split(',')

  return math.sqrt(
    (int(pos1[0]) - int(pos2[0]))**2 +
    (int(pos1[1]) - int(pos2[1]))**2 +
    (int(pos1[2]) - int(pos2[2]))**2
  )

def calculate_box_distances(boxes):
  distances = {}
  for box1 in boxes:
    for box2 in boxes:
      if box1 == box2: continue
      distance = straight_line_distance(box1, box2)
      distances[distance] = [box1, box2]
  return distances

def merge_circuits(circuits):
  final_circuits = []
  for circuit in circuits:
    for i in range(len(final_circuits)):
      final_circuit = final_circuits[i]
      merged_circuit = circuit.intersection(final_circuit)
      if len(merged_circuit) != 0:
        final_circuits[i] = circuit.union(final_circuit)
        break
    else:
      final_circuits.append(circuit)
  return final_circuits

def main():
  junction_boxes = []
  with open("./q8/q8_input.txt", "r") as f:
    for line in f:
      junction_boxes.append(line.strip())

  distance_lookup = calculate_box_distances(junction_boxes)
  distances = list(distance_lookup)
  distances.sort()
  circuits = []

  i = 0
  while (i < 1000):
    smallest_distance = distances[0]
    distances.remove(smallest_distance)
    [box1, box2] = distance_lookup[smallest_distance]
    for circuit in circuits:
      if box1 in circuit and box2 in circuit:
        break
      elif box1 in circuit or box2 in circuit:
        circuit.add(box1)
        circuit.add(box2)
        break
    else:
      circuit = set([box1, box2])
      circuits.append(circuit)
    
    i += 1 

  done = False
  while not done:
    merged_circuits = merge_circuits(circuits)
    if len(merged_circuits) == len(circuits):
      done = True
    circuits = merged_circuits

  largest_three = [0]
  for circuit in circuits:
    if len(circuit) > min(largest_three) and len(largest_three) >= 3:
      largest_three.remove(min(largest_three))
  
    if len(largest_three) < 3:
      largest_three.append(len(circuit))
  
  result = 1
  for size in largest_three:
    result *= size
  print(result)

main()