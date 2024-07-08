array=[3,1,2,23,15]

def insertionSort(array):
    """
    Sorts an array using the Insertion Sort algorithm.
    
    Args:
        array (list): The array to be sorted.
    """
    
    for j in range(1,len(array)):
        # Print the unsorted array
        print("Unsorted array: ",array)
        
        # The key to be inserted
        key=array[j]
        print("key: ",key)
        
        i=j-1
        
        # Shift elements of the array, greater than the key, to the right
        while i>=0 and array[i]>key:
            array[i+1]=array[i]
            i=i-1
            
        # Place the key at its correct position
        array[i+1]=key  
        
        # Print the sorted array
        print("Sorted array: ",array)  
        
insertionSort(array)