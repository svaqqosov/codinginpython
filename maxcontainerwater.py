def findMaxContainerWater(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    while(left < right):
        curr_area = min(arr[left], arr[right]) * (right - left)
        max_area = max(max_area, curr_area)
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
    return max_area


buildings = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = findMaxContainerWater(buildings)
print("Max water container size is {}".format(res))
