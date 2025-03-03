# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
    if len(arr) == 0:
        return -1 # array empty
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    '''Assumes a sorted array'''

    if len(arr) == 0:
        return -1 # array empty
    
    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low+high)//2
        if arr[middle] > target:
            high = middle - 1
        elif arr[middle] < target:
            low = middle + 1
        else:
            return middle

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
    '''Assumes a sorted array'''
  
    middle = (low+high)//2

    if len(arr) == 0:
       return -1 # array empty

    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle)
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle, high)

    return -1
  # TO-DO: add missing if/else statements, recursive calls
