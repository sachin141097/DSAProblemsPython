"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""


def calculate_max_profit(prices, index, memo, can_buy, fee):
    if index == len(prices):
        return 0
    key = (index, can_buy)
    if key in memo:
        return memo[key]
    if can_buy:
        buy = -prices[index] + calculate_max_profit(
            prices, index + 1, memo, not can_buy, fee
        )
        skip = calculate_max_profit(prices, index + 1, memo, can_buy, fee)
        memo[key] = max(buy, skip)
    else:
        sell = (
            prices[index]
            - fee
            + calculate_max_profit(prices, index + 1, memo, not can_buy, fee)
        )
        skip = calculate_max_profit(prices, index + 1, memo, can_buy, fee)
        memo[key] = max(sell, skip)
    return memo[key]


def max_profit(prices, fee):
    memo = {}
    can_buy = True
    return calculate_max_profit(prices, 0, memo, can_buy, fee)


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(max_profit(prices, fee))
