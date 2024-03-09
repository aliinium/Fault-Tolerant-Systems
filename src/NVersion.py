import SortingFunctions

def faultTolerance(array):
    r1 = SortingFunctions.customSort(array)
    r2 = SortingFunctions.binarySort(array)
    r3 = SortingFunctions.bubbleSort(array)
    
    if r1 == r2:
        #print("Final answer with default block.")
        return r1
    
    elif r1 == r3:
        #print("Final answer with default block.")
        return r1
    
    elif r2 == r3:
        #print(f"The default block answer ({r1}) was wrong and the final answer with the replacement block.")
        return r2

nums = [3, 1, 2, 5, 0, 7, 4]

print(faultTolerance(nums))