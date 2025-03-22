"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
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


def max_profit(prices, k):
    memo = {}
    can_buy = True
    total_transactions = k
    return calculate_max_profit(prices, 0, memo, can_buy, total_transactions)


prices = [2, 4, 1]
k = 2
print(max_profit(prices, k))
