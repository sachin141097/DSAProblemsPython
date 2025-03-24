"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""


def lcs(str1, str2, index1, index2, str1_len, str2_len, memo):
    if index1 == str1_len or index2 == str2_len:
        return 0
    key = (index1, index2)
    if key in memo:
        return memo[key]
    if str1[index1] == str2[index2]:
        memo[key] = 1 + lcs(
            str1, str2, index1 + 1, index2 + 1, str1_len, str2_len, memo
        )
    else:
        memo[key] = max(
            lcs(str1, str2, index1, index2 + 1, str1_len, str2_len, memo),
            lcs(str1, str2, index1 + 1, index2, str1_len, str2_len, memo),
        )
    return memo[key]


def find_lcs(text1, text2):
    str1_len = len(text1)
    str2_len = len(text2)
    memo = {}
    return lcs(text1, text2, 0, 0, str1_len, str2_len, memo)


text1 = "abcde"
text2 = "ace"
print(find_lcs(text1, text2))
