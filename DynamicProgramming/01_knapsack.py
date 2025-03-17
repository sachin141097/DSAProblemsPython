def find_max_possible(index, val, weight, W, memo):
    if index >= len(val) or W == 0:
        return 0
    key = (index, W)
    if key in memo:
        return memo[key]
    include_item = val[index] + find_max_possible(
        index + 1, val, weight, W - weight[index], memo
    )
    exclude_item = find_max_possible(index + 1, val, weight, W, memo)
    memo[key] = max(include_item, exclude_item)
    return memo[key]


def find_max_value(val, weight, W):
    memo = {}
    return find_max_possible(0, val, weight, W, memo)


n = int(input(f"Enter the number of items: "))
val = list(map(int, input(f"Enter the value of items: ").split()))
weight = list(map(int, input(f"Enter the weight of the items: ").split()))
W = int(input(f"Enter the knapsack capacity: "))
ans = find_max_value(val, weight, W)
print(f"Maximum value that can be obtained: {ans}")
