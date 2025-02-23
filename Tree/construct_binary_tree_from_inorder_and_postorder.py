"""
This script constructs a binary tree from given inorder and postorder traversals and provides a method to perform level order traversal of the constructed tree.

Classes:
- TreeNode: Represents a node in the binary tree.

Functions:
- construct_binary_tree_from_inorder_and_postorder: Constructs a binary tree from given inorder and postorder traversals.
- levelorder: Performs a level order traversal of the binary tree.

Approach:
1. The `construct_binary_tree_from_inorder_and_postorder` function constructs the binary tree using the following steps:
   - The last element of the postorder list is always the root of the tree.
   - Find the index of this root in the inorder list. This index divides the inorder list into left and right subtrees.
   - Recursively construct the left subtree using the elements before the root index in the inorder list and the corresponding elements in the postorder list.
   - Recursively construct the right subtree using the elements after the root index in the inorder list and the corresponding elements in the postorder list.
   - Combine the left and right subtrees with the root to form the complete tree.
2. The `levelorder` function performs a level order traversal using a queue. It processes each level of the tree one by one and appends the values of the nodes at each level to the result list.

Time Complexity:
- The `construct_binary_tree_from_inorder_and_postorder` function has a time complexity of O(n^2) in the worst case, where n is the number of nodes in the tree. This is because finding the index of the root in the inorder list takes O(n) time, and this operation is performed for each node in the tree.
- However, if we use a hashmap to store the indices of the elements in the inorder list, we can reduce the time complexity to O(n), as the index lookup will take O(1) time.
- The `levelorder` function has a time complexity of O(n), where n is the number of nodes in the tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree_from_inorder_and_postorder(postorder, inorder):
    if not postorder or not inorder:
        return None
    root = TreeNode(postorder[-1])
    root_index = inorder.index(postorder[-1])
    root.left = construct_binary_tree_from_inorder_and_postorder(
        postorder[:root_index], inorder[:root_index]
    )
    root.right = construct_binary_tree_from_inorder_and_postorder(
        postorder[root_index:-1], inorder[root_index + 1 :]
    )
    return root


def levelorder(root):
    if not root:
        return []
    result = []
    queue = []
    queue.append(root)
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


if __name__ == "__main__":
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    root = construct_binary_tree_from_inorder_and_postorder(postorder, inorder)
    print(f"Level order traversal of the constructed tree is: {levelorder(root)}")
