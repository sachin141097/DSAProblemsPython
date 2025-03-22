"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
"""


def calculate_max_profit(prices, index, memo, can_buy, total_transactions):
    if index == len(prices) or total_transactions == 0:
        return 0
    key = (index, can_buy, total_transactions)
    if key in memo:
        return memo[key]
    if can_buy:
        buy = -prices[index] + calculate_max_profit(
            prices, index + 1, memo, not can_buy, total_transactions
        )
        skip = calculate_max_profit(
            prices, index + 1, memo, can_buy, total_transactions
        )
        memo[key] = max(buy, skip)
    else:
        sell = prices[index] + calculate_max_profit(
            prices, index + 1, memo, not can_buy, total_transactions - 1
        )
        skip = calculate_max_profit(
            prices, index + 1, memo, can_buy, total_transactions
        )
        memo[key] = max(sell, skip)
    return memo[key]


def max_profit(prices):
    memo = {}
    can_buy = True
    total_transactions = 2
    return calculate_max_profit(prices, 0, memo, can_buy, total_transactions)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(max_profit(prices))
