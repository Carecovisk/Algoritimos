from algoritimos import *
import timeit, pandas as pd, os
import numpy as np

os.system('cls' if os.name == 'nt' else 'clear')

algoritimos = ["iterative_quickSort","heap_sort", "insertionSort", "mergeSort", "selectionsort","bubblesort",]

print('Escolha um algoritimo:')

for i, algoritimo in enumerate(algoritimos):
    print(f"{algoritimo} ({i})")

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
# Manter compatibilidade com codigo de criação de graficos
resultados[algoritimo] = []

# Input ordenado crecente
stmt = f"{algoritimo}(np.copy(input_ordenado_asc))"
time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
result_asc = (input_size, 'Crecente', time)
print(f"{algoritimo}: {result_asc}")

# Input ordenado decrecente
stmt = f"{algoritimo}(np.copy(input_ordenado_dec))"
time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
result_dec = (input_size, 'Decrecente', time)
print(f"{algoritimo}: {result_dec}")

# Input desordenado
stmt = f"{algoritimo}(np.copy(input_desordenado))"
time = timeit.timeit(stmt=stmt, globals=globals(), number=1)
result_desordenado = (input_size, 'Desordenado', time)
print(f"{algoritimo}: {result_desordenado}")

result = [result_asc, result_dec, result_desordenado]
resultados[algoritimo].append(result)

pd.DataFrame(resultados).to_json(f"./resultados/{algoritimo}_tempos.json")
