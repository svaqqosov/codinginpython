def binarySearch(arr, target):
    left = 0
    right = len(arr) -  1
    while(left <= right):
        mid = (left + right) // 2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,6,7,8,9]
target = 9
result = binarySearch(arr, target)

if result != -1:
    print("Index of the element %d" % result)
else:
    print("Element is not present in the array")
