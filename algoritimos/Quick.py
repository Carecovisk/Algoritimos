
def sort(array,low, high):
    
    if (low < high):
        pivot = hoare(array, low, high)
    
        sort(array,low, pivot)
        sort(array, pivot+1, high)

def hoare(a,l,h):
    pivot = a[l]
    i = l -1
    j = h +1

    while True:
        
        i += 1
        while(a[i] < pivot):
            i += 1

        j -= 1
        while(a[j] > pivot):
            j -= 1
        
        if (i >= j):
            return j

        a[i],a[j] = a[j],a[i]

def lomuto(a, l, h):
    
    pivot = a[h]

    i = (l-1)
    for j in range(l,h):
        if(a[j] <= pivot):

            i +=1
            a[i], a[j] = a[j],a[i]
    a[i +1], a[h] = a[h], a[i +1]
    return i+1

def printArray(array):
    for i in range(len(array)):
        print(array[i],end=" ")
    print()

def quickSort(array):
    sort(array, 0, len(array) - 1)


if __name__ == '__main__':
    a = [10,30,25,5,15]
    b = [0,0,0,0,0]

    print(a)
    sort(a,0,(len(a)-1))

    printArray(a)
    print('\n')

    print(b)
    sort(b,0, (len(b) -1))
    printArray (b)
