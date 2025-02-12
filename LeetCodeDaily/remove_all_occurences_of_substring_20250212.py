"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
"""

"""
Time Complexity: O(N)
"""


def remove_all_occurences(s, part):
    stack = []
    part_len = len(part)
    for char in s:
        stack.append(char)
        if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
            # Remove last `part_len` characters
            del stack[-part_len:]
    return "".join(stack)


if __name__ == "__main__":
    s = input(f"Enter the value of string ")
    part = input(f"Enter the value of part ")
    ans = remove_all_occurences(s, part)
    print(f"Value of {s} after removing all occurences of {part} from it is {ans} ")
