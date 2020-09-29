'''QUICKSORT:
Divide & conquor method: divide into chunks, sort those chunks
STEPS:
1.find a pivot(midpoint, 1st or last element)-starting point, what you will use to compare/sort. should elements be on right or left side
2.partition data around pivot according to right/left(greater,or less than) Will end up with 2 'lists' ONLY PIVOT SORTED HERE
3.repeat steps for left/right lists. (Pick new pivot, partition around pivots)
4.steps will repeat on both sides until sorted around pivots
5.then can concatenate elements together to end with full sorted array
'''
#Divide & conquer
#when writing recursive algorithm:
#1.whats base(ending) case(s)?
#2. if we arent in base case, how are we moving towards the base case(s)?

def partition(data):
    #pick first element in data as pivot
    pivot = data[0]
    left = []
    right = []

    for x in data[1:] #skip first element because its pivot
        if x <= pivot: #if value less or qqual, add to left
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right


def quicksort(data):
    #base case
    if len(data) == 0:
        return data

    #partition handles picking pivot element, and partioning data around pivot
    #left is left sub list
    #pivot is pivot element
    #right is right sub list
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right) #sort left, sort right, add together with pivot in middle

#in place quicksort
def ip_partition(data, start, end):
    # pick the first element in data as our pivot 
    pivot = data[start]
​
    i = start + 1
    j = start + 1
    
    # partitioning step to move elements around the pivot 
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1
​
    data[start], data[i - 1] = data[i - 1], data[start]
    # return the index of the pivot
    return i - 1
​
def ip_quicksort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1
​
    # base case
    # if len(data) == 0:
    if start == end:
        return
​
    # returns the index of the pivot 
    # and partitions the data around the pivot 
    index = ip_partition(data, start, end)
​
    # qs call for everything to the left of the pivot 
    ip_quicksort(data, start, index - 1)
    # qs call for everything to the right of the pivot 
    ip_quicksort(data, index + 1, end)
