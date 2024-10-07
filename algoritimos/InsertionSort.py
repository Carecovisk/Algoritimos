comparacoes = trocas = 0

def insertionSort(value):
    global comparacoes
    global trocas
    
    for i in range(len(value)):
        j = i
        comparacoes += 1
        while (j > 0 and value[j] <= value[j-1]):
            comparacoes += 1
            trocas += 1
            value[j], value[j-1] = value[j-1], value[j]
            j -= 1
    return [comparacoes, trocas]

if __name__ == '__main__':
    a = [1,3,7,9,5]
    b = [5,5,7,3,0,2,1,52,10,6,37]

    print(insertionSort(a))
    print(insertionSort(b))
