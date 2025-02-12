"""
Time Complexity: O(N*d)
"""

from collections import defaultdict


def maximum_sum(nums):
    digit_sum_map = defaultdict(list)
    max_sum = -1
    for num in nums:
        key = digit_sum(num)
        digit_sum_map[key].append(num)
    for values in digit_sum_map.values():
        if len(values) > 1:
            values.sort(reverse=True)
            max_sum = max(max_sum, values[0] + values[1])
    return max_sum


def digit_sum(number):
    return sum(map(int, str(number)))


if __name__ == "__main__":
    nums = list(map(int, input(f"Enter the value of array: ").split()))
    ans = maximum_sum(nums)
    print(ans)
