"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example: "listen" and "silent" are anagrams.
"""

"""
Time Complexity: O(NlogN), where N is the length of the string. We are sorting the string, which takes O(NlogN) time complexity.
"""
if __name__ == "__main__":
    s = input(f"Enter the first string: ")
    t = input(f"Enter the second string: ")
    if sorted(s) == sorted(t):
        print(f"{s} and {t} are anagrams")
    else:
        print(f"{s} and {t} are not anagrams")
