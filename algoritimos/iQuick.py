comparacoes = trocas = 0

def iterative_quickSort(arr):
    global comparacoes
    global trocas
    # Criação de uma pilha simulando o processo recursivo
    stack = [(0, len(arr) - 1)]
    
    # Enquanto houver segmentos na pilha para ordenar
    while stack:
        start, end = stack.pop()

        comparacoes += 1
        if start >= end:
            continue
        
        # Particionar o array e obter o índice do pivô
        pivot_index = partition(arr, start, end)
        
        # Empilhar as duas partes para continuar ordenando
        stack.append((start, pivot_index - 1))  # Parte esquerda do pivô
        stack.append((pivot_index + 1, end))    # Parte direita do pivô

    return [comparacoes, trocas]

def partition(arr, start, end):
    global comparacoes
    global trocas
    # Pivô escolhido como o último elemento
    pivot = arr[end]
    i = start - 1
    
    # Organiza os elementos em torno do pivô
    for j in range(start, end):
        comparacoes += 1
        if arr[j] < pivot:
            i += 1
            trocas += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Coloca o pivô na posição correta
    trocas += 1
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    
    # Retorna o índice do pivô
    return i + 1

