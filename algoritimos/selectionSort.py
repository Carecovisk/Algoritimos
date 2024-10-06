comparacoes = trocas = 0

def selectionsort(lista):
    global comparacoes
    global trocas
    
    for i in range(len(lista) -1):
        imenor = i;
        for f in range(i+1,len(lista)):
            comparacoes += 1
            if lista[f] < lista[imenor]:
                imenor = f

        trocas += 1
        lista[i], lista[imenor] = lista[imenor], lista[i]
    return lista

if __name__ =='__main__':

    a = [9,5,6,7,3,1]
    b = [456,789,123]

    print(selectionsort(a))
    print(selectionsort(b))
