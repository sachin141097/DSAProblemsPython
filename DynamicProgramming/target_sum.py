def total_ways(arr, index, target, memo):
    if index == len(arr):
        return 1 if target == 0 else 0
    key = (index, target)
    if key in memo:
        return memo[key]
    add_element = total_ways(arr, index + 1, target - arr[index], memo)
    remove_element = total_ways(arr, index + 1, target + arr[index], memo)
    memo[key] = add_element + remove_element
    return memo[key]


def find_total_ways(arr, target):
    memo = {}
    return total_ways(arr, 0, target, memo)


arr = list(map(int, input(f"Enter the value of array: ").split()))
target = int(input(f"Enter the value of target: "))
print(target)
print(arr)
no_of_ways = find_total_ways(arr, target)
print(f"No of ways to makeup target {no_of_ways}")
