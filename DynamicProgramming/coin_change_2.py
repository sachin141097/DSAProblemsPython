"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


def count_ways(coins, index, amount, memo):
    if amount == 0:
        return 1
    if amount < 0 or index >= len(coins):
        return 0
    key = (index, amount)
    if key in memo:
        return memo[key]
    include_coin = count_ways(coins, index, amount - coins[index], memo)
    exclude_coin = count_ways(coins, index + 1, amount, memo)
    memo[key] = include_coin + exclude_coin
    return memo[key]


if __name__ == "__main__":
    coins = list(map(int, input(f"Enter the coin denominations: ").split()))
    amount = int(input(f"Enter the amount: "))
    memo = {}
    total_ways = count_ways(coins, 0, amount, memo)
    print(f"Total ways to make the amount from given denominations: {total_ways}")
