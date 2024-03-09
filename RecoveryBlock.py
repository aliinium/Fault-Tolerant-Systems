import SortingFunctions

def faultTolerance(array):
    sortedArrey = SortingFunctions.customSort(nums)
    
    if sum(sortedArrey) == sum(nums):
        #print("Final answer with default block.")   
        return sortedArrey  
    else:
        #print(f"The default block answer ({sortedArrey}) was wrong and the final answer with the replacement block.")
        sortedArrey = SortingFunctions.binarySort(nums)
        return sortedArrey

nums = [3, 1, 2, 5, 0, 7, 4]

print(faultTolerance(nums))