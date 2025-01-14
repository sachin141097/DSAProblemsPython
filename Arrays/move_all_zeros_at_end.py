"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

"""
Time Complexity: O(N), where N is the size of the array. We are iterating through the array once.
"""


def move_zeros(arr):
    n = len(arr)
    left = 0
    for right in range(n):
        if arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    print(arr)


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the value of array elements").split()))
    move_zeros(arr)
