"""
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.



The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.


Example 1
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]

Output: [1, 2, 3, 4, 5, 7]

Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

Example 2
Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]

Output: [1, 3, 4, 5, 6, 7, 8, 9]

Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2
"""

# Time Complexity : O(M+N)
# Visting every element of both the array once


def find_union(arr1, arr2):
    union_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            # Don't add already added elements
            if not union_arr or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            if not union_arr or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1
        else:
            if not union_arr or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        if not union_arr or union_arr[-1] != arr1[i]:
            union_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not union_arr or union_arr[-1] != arr2[j]:
            union_arr.append(arr2[j])
        j += 1
    return union_arr


if __name__ == "__main__":
    arr1 = list(
        map(int, input(f"Enter the elements of array 1 space separated: ").split())
    )
    arr2 = list(
        map(int, input(f"Enter the elements of array 2 space separated: ").split())
    )
    ans = find_union(arr1, arr2)
    print(f"Union of array1 and array2 is {ans}")
