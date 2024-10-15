import random
import time
import matplotlib.pyplot as plt
from math import floor
from copy import deepcopy


def generate_array(length):
  return [random.randint(-999, 999) for _ in range(length)]


def generate_arrays(power):
  return [generate_array(10 ** length) for length in range(1, power + 1)]


def build_plot(power, *sorts):
  unit = 'с'
  count = 0
  colors = ['r', 'b', 'g', 'y', 'm']
  legend = []
  
  arrays = generate_arrays(power)

  x = [10 ** (n + 1) for n in range(power)]

  for sort in sorts:
    temp_arrays = deepcopy(arrays)
    y = []
    legend.append(sort.name)

    for array in temp_arrays:
      y.append(sort.test(array))

    print(f"{sort.name} - {y}")

    if y[-1] < 1:
      y = [value * 1000 for value in y]
      unit = 'мс'

    plt.plot(x, y, f"{colors[count]}o-")

    count += 1

  plt.title(f"{sort.name}")
  plt.xlabel("Количество элементов")
  plt.ylabel(f"Время выполнения, {unit}")
  plt.xscale("log")
  plt.grid(True)
  plt.legend(legend)

  plt.show()


def build_plot_repeating_elements(power, *sorts):
  unit = 'с'
  count = 0
  colors = ['r', 'b', 'g', 'y', 'm']
  legend = []

  arrays = [[random.randint(-998, 999) for _ in range(10 ** length)] for length in range(1, power + 1)]

  rates = [10, 25, 50, 75, 90]

  x = [10 ** (n + 1) for n in range(power)]

  for sort in sorts:
    count = 0
    
    for rate in rates:
      y = []

      legend.append(f"{rate}%")

      temp_arrays = deepcopy(arrays)

      for array in temp_arrays:
        for i in range(len(array) * rate // 100):
          array[i] = -999
        y.append(sort.test(array))

      print(f"{sort.name} {rate}% - {y}")

      if y[-1] < 1:
        y = [value * 1000 for value in y]
        unit = 'мс'

      plt.plot(x, y, f"{colors[count]}o-")

      count += 1

    plt.title(f"{sort.name}")
    plt.xlabel("Количество элементов")
    plt.ylabel(f"Время выполнения, {unit}")
    plt.xscale("log")
    plt.grid(True)
    plt.legend(legend)

    plt.show()


def build_plot_partially_sorted(power, *sorts):
  unit = 'с'
  count = 0
  colors = ['r', 'b', 'g', 'y', 'm']
  legend = []

  arrays = [[random.randint(-999, 999) for _ in range(10 ** length)] for length in range(1, power + 1)]

  parts = [10, 25, 50, 75, 100]
  
  x = [10 ** (n + 1) for n in range(power)]

  for sort in sorts:
    count = 0

    for part in parts:
      y = []

      legend.append(f"{part}%")

      temp_arrays = deepcopy(arrays)

      for array in temp_arrays:
        for i in range(len(array) * part // 100):
          array[i] = i
        y.append(sort.test(array))

      print(f"{sort.name} {part}% - {y}")

      if y[-1] < 1:
        y = [value * 1000 for value in y]
        unit = 'мс'

      plt.plot(x, y, f"{colors[count]}o-")

      count += 1

    plt.title(f"{sort.name}")
    plt.xlabel("Количество элементов")
    plt.ylabel(f"Время выполнения, {unit}")
    plt.xscale("log")
    plt.grid(True)
    plt.legend(legend)

    plt.show()
