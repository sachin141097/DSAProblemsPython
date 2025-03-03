def print_all_subsequences(arr, index, subsequence):
    if index == len(arr):
        print(subsequence)
        return
    # Include the current element
    subsequence.append(arr[index])
    print_all_subsequences(arr, index + 1, subsequence)
    # Exclude the current element
    subsequence.pop()
    print_all_subsequences(arr, index + 1, subsequence)


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the array elements: ").split()))
    print_all_subsequences(arr, 0, [])
