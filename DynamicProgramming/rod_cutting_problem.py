"""
Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.


Examples:
Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8

Output: 25

Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.
"""


def calculate_profit(prices, index, n, memo):
    if index == len(prices):
        return 0
    key = (index, n)
    if key in memo:
        return memo[key]
    not_take = calculate_profit(prices, index + 1, n, memo)
    take = float("-inf")
    rod_length = index + 1
    if rod_length <= n:
        take = prices[index] + calculate_profit(prices, index, n - rod_length, memo)
    memo[key] = max(take, not_take)
    return memo[key]


def find_max_profit(prices, n):
    memo = {}
    return calculate_profit(prices, 0, n, memo)


prices = list(map(int, input(f"Enter the value of prices: ").split()))
n = int(input(f"Enter the rod length: "))
max_profit = find_max_profit(prices, n)
print(f"Maximum possible profit is {max_profit}")
