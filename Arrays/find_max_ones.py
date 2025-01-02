"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.



A binary array is an array that contains only 0s and 1s.


Example 1
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]

Output: 3

Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

Example 2
Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]

Output: 0

Explanation: No 1s are present in nums, thus we return 0
"""


def count_max_ones(arr):
    max_one_count = 0
    one_count_so_far = 0
    for num in arr:
        if not num:
            one_count_so_far = 0
        else:
            one_count_so_far += 1
        max_one_count = max(one_count_so_far, max_one_count)
    return max_one_count


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the elements for binary array: ").split()))
    ans = count_max_ones(arr)
    print(f"Maximum ones in array is {ans}")
