def maxConsecquiteveSum(arr, target):
    window_sum = sum(arr[0: target])
    max_sum = window_sum
    for i in range(0, len(arr) - k):
        print(i)
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [20, -30, 39, 49, 19, 80]
k = 2
result = maxConsecquiteveSum(arr, k)
print("Max subarray of {} elements: {}".format(k, result))