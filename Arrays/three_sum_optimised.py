"""
Time Complexity: O(N^2), where N is the size of the array. We are iterating through the array once and then calling the find_two_sum function which takes O(N) time complexity.
"""


def find_two_sum(arr, target, left, right, triplets):
    while left < right:
        if arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            # Remove duplicates from either end
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1


def find_three_sum(arr):
    n = len(arr)
    if n < 3:
        return []
    arr.sort()
    triplets = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        n1 = arr[i]
        target = -n1
        find_two_sum(arr, target, i + 1, n - 1, triplets)
    return triplets


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the value of array elements: ").split()))
    triplets = find_three_sum(arr)
    print(triplets)
