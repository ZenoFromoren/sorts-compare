# Вставка элемента в массив
def insert_element(array, index, value):
  array.append(None)

  for i in range(len(array) - 1, index - 1, -1):
    array[i] = array[i - 1]

  array[index] = value

  return array


# Удаление элемента из массива
def delete_element(array, index):
  for i in range(index, len(array) - 1):
    array[i] = array[i + 1]

  return array[:-1]


# Найти индекс минимального значения в массиве
def min_value_index(array):
  minValue = array[0]
  minValueIndex = 0

  for i in range(len(array)):
    if array[i] < minValue:
      minValue = array[i]
      minValueIndex = i

  return minValueIndex


# Объединение двух упорядоченных по возрастанию массивов 
# в один с сохранением упорядоченности
def combineOrderedArraysIncreasing(A, B):
  C = []

  lenA = len(A)
  lenB = len(B)

  i = 0
  j = 0

  while len(C) < lenA + lenB:
    if A[i] <= B[j]:
      while A[i] <= B[j]:
        C.append(A[i])
        i += 1
        if i == lenA:
          for n in range(j, lenB):
            C.append(B[n])
          break 
    else:
      while B[j] <= A[i] and j < lenB:
        C.append(B[j])
        j += 1
        if j == lenB:
          for n in range(i, lenA):
            C.append(A[n])
          break

  return C


# Инвертирование массива
def invertArray(array):
  length = len(array)

  for i in range(length // 2):
    array[i], array[length - (i + 1)] = array[length - (i + 1)], array[i]

  return array
