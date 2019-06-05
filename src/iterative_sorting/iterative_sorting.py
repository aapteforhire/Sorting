# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # Swap 
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] # Swap
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr