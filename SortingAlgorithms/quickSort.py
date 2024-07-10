array=[17,15,14,2,3,77,6,19,91,20,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def partition(array, low, high):
    """
    Partitions an array using the pivot element.

    Args:
        array (list): The array to be partitioned.
        low (int): The starting index of the array.
        high (int): The ending index of the array.

    Returns:
        int: The index of the pivot element after partitioning.
    """

    # Choose the last element as the pivot
    pivot = array[high]
    i = low - 1

    # Loop through the array and move elements smaller than the pivot to the left
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot,
        # swap it with the element at the i index and increment i
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap the pivot with the element at the i index
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the index of the pivot element after partitioning
    return i + 1


def quickSort(array,low,high):
    """
    Sorts an array using the Quick Sort algorithm.

    Args:
        array (list): The array to be sorted.
        low (int): The starting index of the array.
        high (int): The ending index of the array.

    Returns:
        list: A sorted array.
    """
    
    # If the array contains more than one element, sort it
    if low<high:
        # Partition the array
        pi=partition(array,low,high)
        
        # Recursively sort the two halves of the array
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)
        
    return array


print("sorted array: ",quickSort(array,0,len(array)-1))
