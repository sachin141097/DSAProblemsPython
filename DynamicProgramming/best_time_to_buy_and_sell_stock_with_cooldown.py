"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
"""


def calculate_max_profit(prices, index, memo, can_buy):
    if index >= len(prices):
        return 0
    key = (index, can_buy)
    if key in memo:
        return memo[key]
    if can_buy:
        buy = -prices[index] + calculate_max_profit(
            prices, index + 1, memo, not can_buy
        )
        skip = calculate_max_profit(prices, index + 1, memo, can_buy)
        memo[key] = max(buy, skip)
    else:
        sell = prices[index] + calculate_max_profit(
            prices, index + 2, memo, not can_buy
        )
        skip = calculate_max_profit(prices, index + 1, memo, can_buy)
        memo[key] = max(sell, skip)
    return memo[key]


def max_profit(prices):
    memo = {}
    can_buy = True
    return calculate_max_profit(prices, 0, memo, can_buy)


prices = [1, 2, 3, 0, 2]
print(max_profit(prices))
