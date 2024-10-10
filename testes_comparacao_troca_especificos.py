from algoritimos import *
import pandas as pd, os
import numpy as np

os.system('cls' if os.name == 'nt' else 'clear')
algoritimos = [iterative_quickSort, heap_sort, insertionSort, mergeSort, selectionsort, bubblesort]
inputs_ordenados_asc, inputs_ordenados_dec, inputs_desordenados = [], [], []

print('Escolha um algoritimo:')

for i, algoritimo in enumerate(algoritimos):
    print(f"{algoritimo.__name__} ({i})")

algoritimo = algoritimos[int(input('Input: '))]

os.system('cls' if os.name == 'nt' else 'clear')

inputs_size = [1_000, 10_000, 50_000, 100_000]

print('Escolha o tamanho da entrada:')
for i, size in enumerate(inputs_size):
    print(f"{size} ({i})")

input_size = inputs_size[int(input('Input: '))]

input_ordenado_asc = np.arange(input_size)
input_ordenado_dec = np.arange(input_size, -1, -1)
input_desordenado = np.random.randint(input_size, size=input_size)

resultados = {}
resultados[algoritimo] = []

# Input ordenado crecente
comparacoes, trocas = algoritimo(np.copy(input_ordenado_asc))
result_asc = ("Crecente", comparacoes, trocas)
print(f"{algoritimo.__name__} {input_size}: {result_asc}")

# Input ordenado decrecente
comparacoes, trocas = algoritimo(np.copy(input_ordenado_dec))
result_dec = ("Decrecente", comparacoes, trocas)
print(f"{algoritimo.__name__} {input_size}: {result_dec}")


# Input desordenado
comparacoes, trocas = algoritimo(np.copy(input_desordenado))
result_desordenado = ("Desordenado", comparacoes, trocas)
print(f"{algoritimo.__name__} {input_size}: {result_desordenado}")

result = [f"Tamanho: {input_size}",result_asc, result_dec, result_desordenado]
resultados[algoritimo].append(result)

pd.DataFrame(resultados).to_json('comparacoes_trocas.json')