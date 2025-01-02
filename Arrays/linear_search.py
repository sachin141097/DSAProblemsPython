def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    arr = list(map(int, input(f"Enter the array elements space separated:").split()))
    target = int(input(f"Enter the value of target element"))
    ans = find_element(arr, target)
    if ans:
        print(f"Element {target} is present at index {ans}")
    else:
        print(f"Element not found in the array")
