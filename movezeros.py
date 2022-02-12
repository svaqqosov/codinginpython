def moveZeros(arr):
    j = 0
    for a in arr:
        if a != 0:
            arr[j] = a
            j += 1
    
    for i in range(j, len(arr)):
        arr[i] = 0
    
    return arr


print(moveZeros([1, 0, 8, 0, 0, 5, -9, 0, 0, 2, 0, 0]))