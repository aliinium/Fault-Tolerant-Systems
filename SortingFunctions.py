def customSort(arr):
    try:
        hasNegative = any(x < 0 for x in arr)
        if hasNegative:
            arr = [-x if x >= 0 else x for x in arr]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    except TypeError as e:
        return f"Error: {e}"
    return arr


def binarySort(arr):
    try:
        for i in range(1, len(arr)):
            key = arr[i]
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1
            
            for j in range(i, left, -1):
                arr[j] = arr[j - 1]
            arr[left] = key
            
    except TypeError as e:
        return f"Error: {e}"
    return arr


def bubbleSort(arr):
    try:
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                
    except TypeError as e:
        return f"Error: {e}"
    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapSort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)
    
    return arr