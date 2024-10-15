from modules import insert_element, delete_element, min_value_index, invertArray, combineOrderedArraysIncreasing
import time


class Sort(object):
  def sort(self):
    pass


  def test(self, *arrays):
    for array in arrays:
      totalRunTime = 0

      for _ in range(3):
        startTime = time.perf_counter()
        self.sort(array)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        totalRunTime += runTime

      runTime = totalRunTime / 3

    return runTime
    

class Selection_sort(Sort):
  name = "Сортировка методом прямой выборки"

  def sort(self, array):
    for i in range(len(array)):
      minValueIndex = min_value_index(array[i:]) + i
      array[minValueIndex], array[i] = array[i], array[minValueIndex]

    return array


class Bubble_sort(Sort):
  name = "Сортировка пузырьком"

  def sort(self, array):
    length = len(array)

    count = 0

    for _ in range(length - 2):
      for i in range(length - 1 - count):
        if array[i] > array[i + 1]:
          array[i], array[i + 1] = array[i + 1], array[i]
      count += 1

    return array


class Insertion_sort(Sort):
  name = "Сортировка простыми вставками"

  def sort(self, array):
    for i in range(1, len(array)):
      j = 0
      if array[i] <= array[i - 1]:
        while array[i] <= array[i - j] and i >= j:
          j += 1
        array = insert_element(array, i - j + 1, array[i])
        array = delete_element(array, i + 1)

    return array


class Gnome_sort(Sort):
  name = "Гномья сортировка"

  def sort(self, array):
    i = 1
    j = 2

    while i < len(array):
      if array[i] > array[i - 1]:
        i = j
        j += 1
      else:
        array[i], array[i - 1] = array[i - 1], array[i]
        i -= 1
        if i == 0:
          i = j
          j += 1

    return array


class Radix_lsd_sort(Sort):
  name = "Цифровая сортировка с младшего разряда"

  def sort(self, array):
    base = 10

    length = len(str(max(array)))

    temps = [[] for _ in range(base)]

    for i in range(length):
      for number in array:
        j = (number // base ** i) % base
        temps[j].append(number)
      array = []
      for sub_array in temps:
        for number in sub_array:
          array.append(number)
      temps = [[] for _ in range(base)]

    return array


class Radix_msd_sort(Sort):
  name = "Цифровая сортировка со старшего разряда"

  def radix_msd_positive(self, array, count = None):
    base = 10

    length = len(str(max(array, default=0)))

    if count == None:
      count = length

    i = length - count

    if i >= length:
      return array

    array_mod = [str(number).zfill(length) for number in array]

    temps = [[] for _ in range(base)]

    for number in array_mod:
      temps[int(number[i])] += [int(number)]

    intermediateResult = []

    for sub_array in temps:
      intermediateResult.append(self.radix_msd_positive(sub_array, count - 1))

    result = []

    for sub_array in intermediateResult:
      result += sub_array

    return result


  def sort(self, array, count = None):
    positiveNumbers = [number for number in array if number >= 0]
    negativeNumbers = [-number for number in array if number < 0]

    return [-number for number in invertArray(self.radix_msd_positive(negativeNumbers))] + self.radix_msd_positive(positiveNumbers)


class Shell_sort(Sort):
  name = "Сортировка Шелла"

  def sort(self, array):
    length = len(array)
    step = length // 2

    while step > 1:
      for i in range(length - step):
        if array[i] > array[i + step]:
          array[i], array[i + step] = array[i + step], array[i]
      step //= 2

    for i in range(1, length):
      j = 0
      if array[i] <= array[i - 1]:
        while array[i] <= array[i - j] and i >= j:
          j += 1
        array = insert_element(array, i - j + 1, array[i])
        array = delete_element(array, i + 1)

    return array


class Quick_sort(Sort):
  name = "Быстрая сортировка"

  def sort(self, array):
    length = len(array)

    if length == 2:
      if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    elif length < 2:
        return array

    referenceValueIndex = length // 2
    referenceValue = array[referenceValueIndex]

    i = 0

    while i < referenceValueIndex:
      if array[i] > referenceValue:
        array = insert_element(array, referenceValueIndex + 1, array[i])
        array = delete_element(array, i)
        referenceValueIndex -= 1
      else:
        i += 1

    for i in range(referenceValueIndex + 1, length):
      if array[i] < referenceValue:
        array = insert_element(array, referenceValueIndex, array[i])
        array = delete_element(array, i + 1)
        referenceValueIndex += 1

    array[:referenceValueIndex] = self.sort(array[:referenceValueIndex])
    array[referenceValueIndex:] = self.sort(array[referenceValueIndex:])

    return array


class Tree_sort(Sort):
  name = "Сортировка деревом"

  def sort(self, array):
    length = len(array)

    for n in range(length - 1):
      step = 2
      dist = step // 2
      while step < length:
        for i in range(n, length - dist, step):
          if array[i] > array[i + dist]:
            array[i], array[i + dist] = array[i + dist], array[i]
        step *= 2
        dist = step // 2

    return array


class Heap_sort(Sort):
  name = "Пирамидальная сортировка"

  def make_heap(array, length, index):
    j = index

    while 2*j + 1 <= length:
      l = 2*j + 1
      r = 2*j + 2

      maxValue = array[l]
      maxValueIndex = l

      if r < length:
        if maxValue < array[r]:
          maxValue = array[r]
          maxValueIndex = r

      if array[j] < maxValue:
        array[j], array[maxValueIndex]= array[maxValueIndex], array[j]

      j = maxValueIndex

    return array


  def sort(self, array):
    length = len(array)

    for i in range(length, -1, -1):
      Heap_sort.make_heap(array, length, i)

    for i in range(length - 1, 0, -1):
      array[0], array[i] = array[i], array[0]
      Heap_sort.make_heap(array, i, 0)

    return array


class Merge_recursive_sort(Sort):
  name = "Рекурсивная сортировка слиянием"

  def sort(self, array):
    length = len(array)

    if length < 2:
      return array
    else:
      center = length // 2
      left = array[:center]
      right = array[center:]
    
      left = self.sort(left)
      right = self.sort(right)

      array = combineOrderedArraysIncreasing(left, right)
  
    return array


class Merge_iterative_sort(Sort):
  name = "Итеративная сортировка слиянием"

  def sort(self, array):
    length = len(array)

    i = 2
    j = 0

    tempArray = []

    while i < length:
      while j < length:
        if j + i <= length:
          newArray = array[j : j + i]
        else:
          newArray = array[j : length]

        newArrayLength = len(newArray)

        if len(newArray) < 2:
          tempArray += newArray
        else:
          left = newArray[: newArrayLength // 2]
          right = newArray[newArrayLength // 2:]

          tempArray += combineOrderedArraysIncreasing(left, right)

        j += i

      j = 0
      i *= 2

      array = tempArray
      tempArray = []

      if i > length:
        left = array[:i // 2]
        right = array[i // 2:]

        array = combineOrderedArraysIncreasing(left, right)

    return array
