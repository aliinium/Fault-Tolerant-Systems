import SortingFunctions

def faultTolerance(array):
    customSort = SortingFunctions.customSort(nums)
    binarySort = SortingFunctions.binarySort(nums)
    bubbleSort = SortingFunctions.bubbleSort(nums)
    heapSort = SortingFunctions.heapSort(nums)

    if(customSort == binarySort):
        r1 = customSort
    else:
        r1 = "Error"

    if(bubbleSort == heapSort):
        r2 = bubbleSort
    else:
        r2 = "Error"

    if(r1 == r2 or r2 == "Error"):
        #print("Final answer with default block.")
        return r1
    else:
        #print(f"The default block answer ({customSort}) was wrong and the final answer with the replacement block.")
        return r2


nums = [3, 1, 2, 5, 0, 7, 4]

print(faultTolerance(nums))