from algoritimos import *
import pandas as pd
import numpy as np

algoritimos = [iterative_quickSort,heap_sort, insertionSort, mergeSort, selectionsort,bubblesort]
inputs_size = [1_000, 10_000, 50_000, 100_000]
inputs_ordenados_asc = []
inputs_ordenados_dec = []
inputs_desordenados = []

for size in inputs_size:
    inputs_ordenados_asc.append(np.arange(size))
    inputs_ordenados_dec.append(np.arange(size, -1, -1))
    inputs_desordenados.append(np.random.randint(size, size=size))

resultados = {}
for algoritimo in algoritimos:
    resultados[algoritimo] = []
    for j, size in enumerate(inputs_size):
        # Input ordenado crecente
        comparacoes, trocas = algoritimo(np.copy(inputs_ordenados_asc[j]))
        result_asc = ("Crecente", comparacoes, trocas)
        print(f"{algoritimo.__name__} {size}: {result_asc}")

        # Input ordenado decrecente
        comparacoes, trocas = algoritimo(np.copy(inputs_ordenados_dec[j]))
        result_dec = ("Decrecente", comparacoes, trocas)
        print(f"{algoritimo.__name__} {size}: {result_dec}")


        # Input desordenado
        comparacoes, trocas = algoritimo(np.copy(inputs_desordenados[j]))
        result_desordenado = ("Desordenado", comparacoes, trocas)
        print(f"{algoritimo.__name__} {size}: {result_desordenado}")

        result = [f"Tamanho: {size}",result_asc, result_dec, result_desordenado]
        resultados[algoritimo].append(result)

pd.DataFrame(resultados).to_json('comparacoes.json')