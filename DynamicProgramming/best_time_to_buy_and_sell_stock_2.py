"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
"""


def calculate_max_profit(prices, index, can_buy, memo):
    if index >= len(prices):
        return 0
    key = (index, can_buy)
    if key in memo:
        return memo[key]
    if can_buy:
        buy = -prices[index] + calculate_max_profit(
            prices, index + 1, not can_buy, memo
        )
        skip = calculate_max_profit(prices, index + 1, can_buy, memo)
        memo[key] = max(buy, skip)
    else:
        sell = prices[index] + calculate_max_profit(
            prices, index + 1, not can_buy, memo
        )
        skip = calculate_max_profit(prices, index + 1, not can_buy, memo)
        memo[key] = max(sell, skip)
    return memo[key]


def max_profit(prices):
    can_buy = True
    memo = {}
    return calculate_max_profit(prices, 0, can_buy, memo)


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
