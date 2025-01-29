def maximum_points(card_points, k):
    n = len(card_points)
    left_sum = 0
    right_sum = 0
    max_points = 0
    for i in range(k):
        left_sum += card_points[i]
    max_points = left_sum
    right_index = n - 1
    for i in range(k - 1, -1, -1):
        right_sum += card_points[right_index]
        left_sum -= card_points[i]
        max_points = max(max_points, left_sum + right_sum)
        right_index -= 1
    return max_points


if __name__ == "__main__":
    card_points = list(
        map(int, input(f"Enter the value of card points separated by space: ").split())
    )
    k = int(input(f"Enter the value of k: "))
    ans = maximum_points(card_points, k)
    print(f"Maxmimum Points that can be obtained {ans}")
