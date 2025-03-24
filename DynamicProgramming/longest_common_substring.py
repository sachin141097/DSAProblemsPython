"""
Given two strings str1 and str2, find the length of their longest common substring.



A substring is a contiguous sequence of characters within a string.


Examples:
Input: str1 = "abcde", str2 = "abfce"

Output: 2

Explanation: The longest common substring is "ab", which has a length of 2.

Input: str1 = "abcdxyz", str2 = "xyzabcd"

Output: 4

Explanation: The longest common substring is "abcd", which has a length of 4.
"""


def find_longest_common_substring(
    str1, str2, index1, index2, str1_len, str2_len, memo, current_length
):
    if index1 == str1_len or index2 == str2_len:
        return current_length
    key = (index1, index2, current_length)
    if key in memo:
        return memo[key]
    if str1[index1] == str2[index2]:
        current_length = find_longest_common_substring(
            str1,
            str2,
            index1 + 1,
            index2 + 1,
            str1_len,
            str2_len,
            memo,
            current_length + 1,
        )
    option1 = find_longest_common_substring(
        str1, str2, index1 + 1, index2, str1_len, str2_len, memo, 0
    )
    option2 = find_longest_common_substring(
        str1, str2, index1, index2 + 1, str1_len, str2_len, memo, 0
    )
    memo[key] = max(current_length, option1, option2)
    return memo[key]


def longest_common_substring(str1, str2):
    memo = {}
    str1_len = len(str1)
    str2_len = len(str2)
    return find_longest_common_substring(str1, str2, 0, 0, str1_len, str2_len, memo, 0)


str1 = "abcde"
str2 = "abfce"
print(longest_common_substring(str1, str2))
