def find_max(arr):
    largest = float("-inf")
    for num in arr:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    arr = list(
        map(int, input(f"Enter the array elements separated by space: ").split())
    )
    ans = find_max(arr)
    print(f"Max value from array is {ans}")
