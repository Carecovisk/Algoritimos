from algoritimos import *
import matplotlib.pyplot as plt
import timeit, sys, pandas as pd
import numpy as np

sys.setrecursionlimit(100000)

algoritimos = ["iterative_quickSort","heap_sort","bubblesort", "insertionSort", "mergeSort", "selectionsort"]
inputs_size = [1_000, 10_000, 50_000, 100_000]
inputs_ordenados_asc = []
inputs_ordenados_dec = []
inputs_desordenados = []

for size in inputs_size:
    inputs_ordenados_asc.append(np.arange(size))
    inputs_ordenados_dec.append(np.arange(size, -1, -1))
    inputs_desordenados.append(np.random.randint(size, size=size))


i = 0
j = 1

print(inputs_ordenados_asc[j][:10])

stmt = f"{algoritimos[i]}(inputs_ordenados_asc[j])"
# stmt = f"{algoritimos[i]}(inputs_ordenados_asc[j])"
time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
result_asc = time
print(f"{algoritimos[i]}: {result_asc}")
