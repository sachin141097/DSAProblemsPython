def find_longest_increasing_subsequence(arr):
    n = len(arr)
    memo = [[-1] * (n + 1) for _ in range(n)]
    return longest_increasing_subsequence(arr, 0, -1, memo)


def longest_increasing_subsequence(arr, index, prev_index, memo):
    n = len(arr)
    if index == n:
        return 0
    if memo[index][prev_index + 1] != -1:
        return memo[index][prev_index + 1]
    # Skip the current element
    not_pick = longest_increasing_subsequence(arr, index + 1, prev_index, memo)
    # pick the current element if it is greater than previous
    pick = 0
    if prev_index == -1 or arr[index] > arr[prev_index]:
        pick = 1 + longest_increasing_subsequence(arr, index + 1, index, memo)
    memo[index][prev_index + 1] = max(pick, not_pick)
    return memo[index][prev_index + 1]


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the value of array: ").split()))
    result = find_longest_increasing_subsequence(arr)
    print(f"Length of longest increasing subsequence is {result}")
