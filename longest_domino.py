def get_longest_chain(dominoes):
  result = []
  unique = []
  for i in range(len(dominoes)):
    for j in range(i+1, len(dominoes)):
      if dominoes[i][1] == dominoes[j][0]:
        result.append(dominoes[i])
        result.append(dominoes[j])
      elif dominoes[i][1] == dominoes[j][1]:
        data = [dominoes[j][1], dominoes[j][0]]
        result.append(dominoes[i])
        result.append(data)
  for item in result:
    if item not in unique:
      unique.append(item)
  return unique
print(get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]))
print(get_longest_chain([[2, 1], [4, 3], [5, 3]]))
print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))
print(get_longest_chain([[6, 6], [6, 1], [1, 1], [0, 3], [2, 3], [4, 1], [5, 6]]))
print(get_longest_chain([[0, 4], [3, 3], [0, 3], [5, 6], [4, 5], [4, 2], [5, 5], [1, 2], [4, 4]]))