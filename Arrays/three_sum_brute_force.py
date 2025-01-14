"""
Given an integer array nums.Return all triplets such that:

i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.


Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.


Example 1
Input: nums = [2, -2, 0, 3, -3, 5]

Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

Explanation: nums[1] + nums[2] + nums[0] = 0

nums[4] + nums[1] + nums[5] = 0

nums[4] + nums[2] + nums[3] = 0

Example 2
Input: nums = [2, -1, -1, 3, -1]

Output: [[-1, -1, 2]]

Explanation: nums[1] + nums[2] + nums[0] = 0

Note that we have used two -1s as they are separate elements with different indexes

But we have not used the -1 at index 4 as that would create a duplicate triplet
"""

"""
Time Complexity: O(N3 x log(no. of unique triplets)), where N is size of the array. Using 3 nested loops & inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

Space Complexity: O(2 x no. of the unique triplets) for using a set data structure and a list to store the triplets.
"""


def three_sum(nums):
    n = len(nums)
    triplet_set = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    # sorting the triplets to ensure uniqueness when storing in set
                    temp.sort()
                    triplet_set.add(tuple(temp))
    return [list(triplet) for triplet in triplet_set]


if __name__ == "__main__":
    nums = list(map(int, input(f"Enter the value of array elements: ").split()))
    ans = three_sum(nums)
    print(ans)
