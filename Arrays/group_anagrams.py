"""
Given an array of strings group the anagrams together.You can return the answer in any order.
Example:
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""

"""
Time Complexity
Outerloop iterates over all the strings in the list, so it takes O(N) time.

Inner loop for each string it uses another loop to compare with all other strings, so it takes O(N) time.

For eachh pair of strings we are checking if they are anagrams or not. This takes O(m) time, where m is the length of the string.

So,overall time complexity is O(N^2 * m), where N is the number of strings in the list and m is the length of the string.
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


def group_anagrams(strs):
    n = len(strs)
    visited = [False] * n
    final_list = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        temp_list = [strs[i]]
        for j in range(i + 1, n):
            if visited[j]:
                continue
            if is_anagram(strs[i], strs[j]):
                temp_list.append(strs[j])
                visited[j] = True
        final_list.append(temp_list)
    return final_list


if __name__ == "__main__":
    # take input list from user
    strs = list(
        map(str, input(f"Enter the list of strings separated by space:").split())
    )
    # final list which has all anagrams grouped toegether
    final_list = []
    final_list = group_anagrams(strs)
    print(final_list)
