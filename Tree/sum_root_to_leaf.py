"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def calculate_path_sum(root, path_sum):
    if root is None:
        return 0
    path_sum = 10 * path_sum + root.val
    if root.left is None and root.right is None:
        return path_sum
    return calculate_path_sum(root.left, path_sum) + calculate_path_sum(
        root.right, path_sum
    )


def sum_root_to_leaf(root):
    return calculate_path_sum(root, 0)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    total_sum = sum_root_to_leaf(root)
    print(f"Total sum of all root-to-leaf numbers: {total_sum}")
