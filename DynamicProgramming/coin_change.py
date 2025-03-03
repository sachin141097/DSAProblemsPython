def min_coins_required(coins, index, target, memo):
    # If target becomes 0 no coins are needed
    if target == 0:
        return 0

    # If target is negative or no coins are left not possible
    if target < 0 or index >= len(coins):
        return float("inf")
    key = (index, target)
    if key in memo:
        return memo[key]

    # Include the current coin and stay at the same index
    include_coin = 1 + min_coins_required(coins, index, target - coins[index], memo)

    # Exclude current coin and give chance to other coins
    exclude_coin = min_coins_required(coins, index + 1, target, memo)
    memo[key] = min(include_coin, exclude_coin)
    return memo[key]


if __name__ == "__main__":
    n = int(input(f"Enter the number of coins: "))
    print(f"Enter the coin denominations: ")
    coins = list(map(int, input().split()))
    target = int(input(f"Enter the target sum: "))
    memo = {}
    result = min_coins_required(coins, 0, target, memo)
    if result == float("inf"):
        result = -1
    print(f"Min coins required to make {target} are {result}")
