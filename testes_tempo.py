from algoritimos import *
import timeit, pandas as pd
import numpy as np

algoritimos = ["iterative_quickSort","heap_sort", "insertionSort", "mergeSort", "selectionsort","bubblesort",]
inputs_size = [1_000, 10_000, 50_000, 100_000]
inputs_ordenados_asc, inputs_ordenados_dec, inputs_desordenados = [], [], []

for size in inputs_size:
    inputs_ordenados_asc.append(np.arange(size))
    inputs_ordenados_dec.append(np.arange(size, -1, -1))
    inputs_desordenados.append(np.random.randint(size, size=size))

resultados = {}
for algoritimo in algoritimos:
    resultados[algoritimo] = []
    for j, size in enumerate(inputs_size):
        # Input ordenado crecente
        stmt = f"{algoritimo}(np.copy(inputs_ordenados_asc[{j}]))"
        time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
        result_asc = (size, 'Crecente', time)
        print(f"{algoritimo}: {result_asc}")

        # Input ordenado decrecente
        stmt = f"{algoritimo}(np.copy(inputs_ordenados_dec[{j}]))"
        time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
        result_dec = (size, 'Decrecente', time)
        print(f"{algoritimo}: {result_dec}")

        # Input desordenado
        stmt = f"{algoritimo}(np.copy(inputs_desordenados[{j}]))"
        time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
        result_desordenado = (size, 'Desordenado', time)
        print(f"{algoritimo}: {result_desordenado}")

        result = [result_asc, result_dec, result_desordenado]
        resultados[algoritimo].append(result)

pd.DataFrame(resultados).to_json('tempos.json')
