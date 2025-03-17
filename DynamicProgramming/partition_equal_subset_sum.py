"""
Given an array arr of n integers, return true if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal else return false.


Examples:
Input: arr = [1, 10, 21, 10]

Output: True

Explanation: The array can be partitioned as [1, 10, 10] and [21].
"""


def is_subset_sum(arr, index, target, memo):
    if target == 0:
        return True
    if index >= len(arr) or target < 0:
        return False
    key = (index, target)
    if key in memo:
        return memo[key]
    include = is_subset_sum(arr, index + 1, target - arr[index], memo)
    exclude = is_subset_sum(arr, index + 1, target, memo)
    memo[key] = include or exclude
    return memo[key]


def is_partition_possible(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    memo = {}
    return is_subset_sum(arr, 0, target, memo)


arr = list(map(int, input(f"Enter the value of array elements: ").split()))
print(is_partition_possible(arr))
