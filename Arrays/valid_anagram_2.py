"""
Check if given two strings are anagrams or not without sorting
"""

"""
Time Complexity: O(N), where N is the length of the string. We are iterating through the string and counting the frequency of each character.
"""


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s1 = [0] * 26
    s2 = [0] * 26
    for i in range(len(s)):
        s1[ord(s[i]) - ord("a")] += 1
        s2[ord(t[i]) - ord("a")] += 1
    return s1 == s2


if __name__ == "__main__":
    s = input(f"Enter the first string: ")
    t = input(f"Enter the second string: ")
    ans = is_anagram(s, t)
    if ans:
        print(f"{s} and {t} are anagrams")
    else:
        print(f"{s} and {t} are not anagrams")
