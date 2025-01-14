"""
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in non-decreasing order.


Example 1
Input: nums = [1, 6, 2, 10, 3], target = 7

Output: [0, 1]

Explanation: nums[0] + nums[1] = 1 + 6 = 7

Example 2
Input: nums = [1, 3, 5, -7, 6, -3], target = 0

Output: [1, 5]

Explanation: nums[1] + nums[5] = 3 + (-3) = 0
"""

"""
Complexity Analysis 
Time Complexity:O(N), where N is the size of the array. The loop runs N times in the worst case and searching in a hashmap takes O(1) generally. So the time complexity is O(N).

Note:In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. In that case, the time complexity will be O(N2). If we use map instead of unordered_map, the time complexity will be O(N* logN) as the map data structure takes logN time to find an element.

Space Complexity: O(N) for using the map data structure.
"""


def find_two_sum(nums, target):
    m = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if m.get(complement) is not None:
            return [m.get(complement), i]
        m[nums[i]] = i
    return []


if __name__ == "__main__":
    nums = list(map(int, input(f"Enter the value of array eleements: ").split()))
    target = int(input(f"Enter the value of target: "))
    ans = find_two_sum(nums, target)
    print(ans)
