"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


# def findPositions(nums, target):
#     l = 0
#     r = len(nums) - 1
#     res = [-1, -1]
#     while(l <= r):
#         m = (l + r) // 2
#         if nums[m] < target:
#             l = m + 1
#         elif nums[m] > target:
#             r = m - 1
#         else:
#             for i in reversed(range(0, m + 1)):
#                 if nums[i] == target:
#                     res[0] = i
#                     i -= 1
#                 else:
#                     break
#             for i in range(m, len(nums)):
#                 if nums[i] == target:
#                     res[1] = i
#                     i += 1
#                 else:
#                     break
#             break
#     return res


def findLeftPostion(nums, target):
    l = 0
    r = len(nums) - 1
    while(l <= r):
        m = (l + r) // 2
        if nums[m] == target:
            if m == 0 or nums[m - 1] != target:
                return m
            r = m - 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


def findRightPosition(nums, target):
    l = 0
    r = len(nums) - 1
    while(l <= r):
        m = (l + r) // 2
        if nums[m] == target:
            if m == len(nums) - 1 or nums[m + 1] != target:
                return m
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


def findPositions(nums, target):
    left = findLeftPostion(nums, target)
    right = findRightPosition(nums, target)
    return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 3

res = findPositions(nums, target)
print(res)
