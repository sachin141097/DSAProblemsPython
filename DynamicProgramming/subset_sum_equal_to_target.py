"""
Given an array arr of n integers and an integer target, determine if there is a subset of the given array with a sum equal to the given target.


Examples:
Input: arr = [1, 2, 7, 3], target = 6

Output: True

Explanation: There is a subset (1, 2, 3) with sum 6.
"""


def is_subset_sum(arr, n, target, memo):
    if target == 0:
        return True
    if n == 0:
        return False
    key = (n, target)
    if key in memo:
        return memo[key]
    include = is_subset_sum(arr, n - 1, target - arr[n - 1], memo)
    exclude = is_subset_sum(arr, n - 1, target, memo)
    memo[key] = include or exclude
    return memo[key]


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the array elements: ").split()))
    target = int(input(f"Enter the target sum: "))
    memo = {}
    if is_subset_sum(arr, len(arr), target, memo):
        print("True")
    else:
        print("False")
