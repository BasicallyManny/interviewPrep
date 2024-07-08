def merge(leftArray, rightArray):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        leftArray (list): The first sorted array.
        rightArray (list): The second sorted array.
    
    Returns:
        list: A single sorted array containing all elements from leftArray and rightArray.
    """
    
    # Initialize the indices for the left and right arrays
    i = j = 0
    
    # Initialize an empty list to store the merged array
    result = []

    # Print the initial arrays
    print("leftArray: ", leftArray)
    print("rightArray: ", rightArray)

    # Merge the arrays
    while(len(leftArray) > i and len(rightArray) > j):
        # If the element from the left array is smaller, append it to the result
        if leftArray[i] < rightArray[j]:
            print("leftArray[",i,"]: ", leftArray[i])
            result.append(leftArray[i])
            i += 1
        # Otherwise, append the element from the right array
        else:
            print("rightArray[",j,"]: ", rightArray[j])
            result.append(rightArray[j])
            j += 1

    # Append the remaining elements from the left array
    result.extend(leftArray[i:])
    
    # Append the remaining elements from the right array
    result.extend(rightArray[j:])

    # Print the merged array
    print("result: ", result) 

    # Return the merged array
    return result

def mergeSort(array):
    """
    Sorts an array using the Merge Sort algorithm.
    
    Args:
        array (list): The array to be sorted.
    
    Returns:
        list: A sorted array.
    """
    
    # Base case: if array length is 1 or less, return it
    if len(array) <= 1:
        print("Returning array of length 1 or less")
        return array
    
    # Divide the array into two halves
    arrayOne = array[:len(array)//2]
    arrayTwo = array[len(array)//2:]
    
    # Recursively sort the two halves
    print("Sorting array one: ", arrayOne)
    arrayOne = mergeSort(arrayOne)
    print("Sorting array two: ", arrayTwo)
    arrayTwo = mergeSort(arrayTwo)
    
    # Merge the two sorted halves into a single sorted array
    print("Merging array one and two")
    mergedArray = merge(arrayOne, arrayTwo)
    
    # Return the merged array
    return mergedArray
        
#Test merge sort function
array=[12,15,17,20,1,4,51,90,17,17]
print("merged array: ", mergeSort(array))

    