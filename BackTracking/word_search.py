"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

"""
Time Complexity: O(N x M x 4^L), where N is the number of rows, M is the number of columns, and L is the length of the word. We are iterating through all the cells of the board and for each cell, we are checking in all 4 directions for the word. The maximum length of the word can be L, so the time complexity is O(N x M x 4^L).
Space Complexity: O(L), where L is the length of the word. The space complexity is O(L) due to the recursive stack space used for the backtracking algorithm.
"""


def find(board, row, col, word, index, total_rows, total_cols):
    if index == len(word):
        return True
    # out of boundary condition check or if the cell value is not equal to the word character or if the letter is already visited
    if (
        row < 0
        or row >= total_rows
        or col <= 0
        or col >= total_cols
        or board[row][col] != word[index]
        or board[row][col] == "#"
    ):
        return False
    temp = board[row][col]
    board[row][col] = "#"  # marking the cell as visited
    # check for the next character in the word in all 4 directions
    if (
        find(board, row + 1, col, word, index + 1, total_rows, total_cols)
        or find(board, row - 1, col, word, index + 1, total_rows, total_cols)
        or find(board, row, col + 1, word, index + 1, total_rows, total_cols)
        or find(board, row, col - 1, word, index + 1, total_rows, total_cols)
    ):
        return True
    board[row][col] = temp  # marking the cell as unvisited
    return False


def exist(board, word):
    total_rows = len(board)
    total_cols = len(board[0])
    for row in range(total_rows):
        for col in range(total_cols):
            if board[row][col] == word[0] and find(
                board, row, col, word, 0, total_rows, total_cols
            ):
                return True
    return False


if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    board = []
    print(f"Enter the elements of the board row wise:")
    for _ in range(rows):
        row = input().strip().split()
        if len(row) != cols:
            print("Invalid input")
            exit()
        board.append(list(row))
    print(f"The input grid is:")
    for row in board:
        print(" ".join(row))
    word = input(f"Enter the word to seach in the grid:")
    ans = exist(board, word)
    if ans:
        print(f"Word {word} exists in the grid")
    else:
        print(f"Word {word} doesn't exist in the grid")
