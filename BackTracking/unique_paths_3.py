"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
"""

"""
Time Complexity: O(4^N), where N is the number of cells in the grid. We are iterating through all the cells of the grid and for each cell, we are checking in all 4 directions. The maximum length of the path can be N, so the time complexity is O(4^N).
"""


def back_track(
    grid, start_x, start_y, non_obstacles, current_count, result, total_rows, total_cols
):
    if (
        start_x < 0
        or start_x >= total_rows
        or start_y < 0
        or start_y >= total_cols
        or grid[start_x][start_y] == -1
    ):
        return
    if grid[start_x][start_y] == 2:
        if current_count == non_obstacles:
            result[0] += 1
        return
    # visit the cell
    grid[start_x][start_y] = -1
    # move in all 4 directions
    back_track(
        grid,
        start_x + 1,
        start_y,
        non_obstacles,
        current_count + 1,
        result,
        total_rows,
        total_cols,
    )
    back_track(
        grid,
        start_x - 1,
        start_y,
        non_obstacles,
        current_count + 1,
        result,
        total_rows,
        total_cols,
    )
    back_track(
        grid,
        start_x,
        start_y + 1,
        non_obstacles,
        current_count + 1,
        result,
        total_rows,
        total_cols,
    )
    back_track(
        grid,
        start_x,
        start_y - 1,
        non_obstacles,
        current_count + 1,
        result,
        total_rows,
        total_cols,
    )
    # backtrack
    grid[start_x][start_y] = 0


def find_unique_paths(grid):
    total_rows = len(grid)
    total_cols = len(grid[0])
    non_obstacles = 0
    start_x = 0
    start_y = 0
    result = [0]
    for row in range(total_rows):
        for col in range(total_cols):
            if grid[row][col] == 0:
                non_obstacles += 1
            if grid[row][col] == 1:
                start_x = row
                start_y = col
    non_obstacles += 1  # Starting cell is also non obstacle
    current_count = 0
    back_track(
        grid,
        start_x,
        start_y,
        non_obstacles,
        current_count,
        result,
        total_rows,
        total_cols,
    )
    return result[0]


if __name__ == "__main__":
    m = int(input(f"Enter number of rows:"))
    n = int(input(f"Enter number of columns:"))
    grid = []
    for i in range(m):
        grid.append(list(map(int, input(f"Enter row {i+1} elements").split())))
    print(grid)
    ans = find_unique_paths(grid)
    print(f"Number of unique paths are {ans}")
