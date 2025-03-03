"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
"""


def min_cost(days, costs, index, memo):
    # If we have covered all travel days no need to travel and spend
    if index >= len(days):
        return 0
    if memo[index] != -1:
        return memo[index]
    # Option 1: Buy a one day pass
    choice_1 = costs[0] + min_cost(days, costs, index + 1, memo)
    # Option 2: Buy a 7 day pass
    i = index
    while i < len(days) and days[i] < days[index] + 7:
        i += 1
    choice_2 = costs[1] + min_cost(days, costs, i, memo)

    # Option 3: Buy a 30 day pass
    i = index
    while i < len(days) and days[i] < days[index] + 30:
        i += 1
    choice_3 = costs[2] + min_cost(days, costs, i, memo)
    memo[index] = min(choice_1, choice_2, choice_3)
    return memo[index]


def min_cost_for_tickets(days, costs):
    n = len(days)
    memo = [-1] * n
    return min_cost(days, costs, 0, memo)


if __name__ == "__main__":
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    print(min_cost_for_tickets(days, costs))
