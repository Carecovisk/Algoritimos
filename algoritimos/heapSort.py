comparacoes = trocas = 0

def heapify(arr, n, i):
    global comparacoes
    global trocas
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

    comparacoes += 1
    # Se o filho na esquerda é maior
    if left < n and arr[left] > arr[parent]:
        parent = left

    comparacoes += 1
    # Se o filho na direita é maior
    if right < n and arr[right] > arr[parent]:
        parent = right

    if parent != i:
        trocas += 1
        arr[i], arr[parent] = arr[parent], arr[i]  # Troca
        heapify(arr, n, parent)

def heap_sort(arr):
    global comparacoes
    global trocas
    n = len(arr)

    # Constrói o Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        trocas += 1
        # Move a raiz atual para o final
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)
    
    return [comparacoes, trocas]
