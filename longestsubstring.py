"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


def findLongestSubstring(s):
    left = 0
    right = 0
    n = len(s)
    res = 0
    map = {}
    while(left < n and right < n):
        el = s[right]
        if el in map:
            left = map[el] + 1
        map[el] = right
        res = max(res, (right - left) + 1)
        right += 1
    return res


s = "abaacad"
ans = findLongestSubstring(s)
print("longest substring: {} ".format(ans))
