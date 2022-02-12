def isValidMountainArray(arr):
    i = 1
    size = len(arr)
    if size < 3:
        return False
    while i < size and arr[i] > arr[i - 1]:
        i += 1
    if i == 1 or i == size:
        return False
    while i < size and arr[i] < arr[i - 1]:
        i += 1
    return i == size


print(isValidMountainArray([1, 2, 3, 4, 3, 2, 1]))
