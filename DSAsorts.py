#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(arr):
    print("Initial Array")
    print(arr)
    size = len(arr)

    for i in range(size):
        for j in range(0,size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1]= temp
    print("Sorted Array")
    print(arr)
    return arr

def insertionSort(arr):
    size = len(arr)
    i = 1
    for i in range(size):
        j = i
        while(j > 0) and (arr[j-1]> arr[j]):
            temp = arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp

            j= j-1
    print("Sorted Array")
    print(arr)
    return arr


def selectionSort(arr):
    size = len(arr)

    for i in range(size-1):
        minVal = i
        for j in range(i+1, size):
            if arr[j] < arr[minVal]:
                minVal = j
        temp = arr[minVal]
        arr[minVal] = arr[i]
        arr[i] = temp
    print("Sorted Array")
    print(arr)
    return arr

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


