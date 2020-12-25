import sys
def maxConsecquiteveSum(arr, k):
    max_sum = -sys.maxsize - 1
    n = len(arr)
    for i in range(0, n - k + 1):
        print(i)
        curr_sum = 0
        for j in range(0, k):
            curr_sum += arr[i + j]
            max_sum = max(curr_sum, max_sum)
    return max_sum


arr = [10, 4, -9, 30, -7, 50, 2]
k = 2

res = maxConsecquiteveSum(arr, k)
print("Max consecquiteve sum of {} elements of array is: {}".format(k, res))