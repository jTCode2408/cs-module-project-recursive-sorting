import sys
sys.setrecursionlimit(1500)
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    #pivots for both arr
    a_pivot = 0
    b_pivot = 0


    


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) >1: 
        middle = len(arr)//2 #Finding the midpoint of the array 
        left = arr[:middle] # define left/right sublists 
        right = arr[middle:]  
        merge_sort(left) # sort left recursive
        merge_sort(right) # sort recursively
  
        i = j = k = 0 #indexes for left right mid
        # Copy data sub lists 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
          
        # Checking if any element was left(bas) 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
