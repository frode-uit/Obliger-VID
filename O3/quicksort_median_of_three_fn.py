from random import randint
import statistics

def get_median_of_three(array):
    pa = [0] * 3
    pa[0] = array[0]
    pa[1] = array[-1]
    pa[2] = array[len(array)//2]
    pa.sort()
    return pa[1]

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` as median of three
    # from the first, last and middle element
    # pivot = statistics.median(array) # use lib function
    pivot = get_median_of_three(array)
    
    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

l = [9,8,7,6,5,4,3,2,1,0]
print(quicksort(l))
