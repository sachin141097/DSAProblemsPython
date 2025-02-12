"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
"""

"""
Time Complexity: O(N^2*d)
"""


def is_sum_of_digits_equal(n1, n2):
    sum_n1 = sum(map(int, str(n1)))
    sum_n2 = sum(map(int, str(n2)))
    return sum_n1 == sum_n2


def maximum_sum(nums):
    max_sum = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if is_sum_of_digits_equal(nums[i], nums[j]):
                max_sum = max(nums[i] + nums[j], max_sum)
    return max_sum


if __name__ == "__main__":
    nums = list(map(int, input(f"Enter the value of array: ").split()))
    ans = maximum_sum(nums)
    print(ans)
