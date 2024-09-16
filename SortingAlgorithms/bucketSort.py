list=[1.42, 2.32, 3.33, 12.52, .37, 1.47, 4.51]

##Insertion Sort for sorting each bucket but any sorting algorithm can be used
def insertionSort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            j -= 1
        bucket[j + 1] = key

def bucketSort(arr):
    n = len(arr)
    
    if n == 0:
        return arr
    
    # Find the maximum value in the array to normalize the range
    max_val = max(arr)
    
    # Create n empty buckets
    buckets = [[] for _ in range(n)]
    
    # Normalize the array by dividing by max_val and put elements into buckets
    for num in arr:
        normalized_index = int((num / max_val) * (n - 1))  # Normalize and avoid index out of range
        buckets[normalized_index].append(num)

    # Sort individual buckets using insertion sort
    for bucket in buckets:
        insertionSort(bucket)

    # Concatenate all buckets into arr[]
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

            
bucketSort(list) 
print("Sorted array is:")
print(" ".join(map(str, list)))