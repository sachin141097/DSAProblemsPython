class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to construct a binary tree from given inorder and preorder traversals
def construct_binary_tree_from_inorder_and_preorder(preorder, inorder):
    # Base case: if either preorder or inorder list is empty, return None
    if not preorder or not inorder:
        return None

    # The first element of preorder list is the root of the tree
    root = TreeNode(preorder[0])

    # Find the index of the root in inorder list
    root_index = inorder.index(preorder[0])

    # Recursively construct the left subtree
    root.left = construct_binary_tree_from_inorder_and_preorder(
        preorder[1 : root_index + 1], inorder[:root_index]
    )

    # Recursively construct the right subtree
    root.right = construct_binary_tree_from_inorder_and_preorder(
        preorder[root_index + 1 :], inorder[root_index + 1 :]
    )

    # Return the constructed tree
    return root


# Function to perform level order traversal of the binary tree
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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = construct_binary_tree_from_inorder_and_preorder(preorder, inorder)
    print(f"Level order traversal of the constructed tree is: {levelorder(root)}")

# Approach:
# 1. The first element of the preorder list is always the root of the tree.
# 2. Find the index of this root in the inorder list. This index divides the inorder list into left and right subtrees.
# 3. Recursively construct the left subtree using the elements before the root index in the inorder list and the corresponding elements in the preorder list.
# 4. Recursively construct the right subtree using the elements after the root index in the inorder list and the corresponding elements in the preorder list.
# 5. Combine the left and right subtrees with the root to form the complete tree.

# Time Complexity:
# The time complexity of this approach is O(n^2) in the worst case, where n is the number of nodes in the tree. This is because finding the index of the root in the inorder list takes O(n) time, and this operation is performed for each node in the tree.
# However, if we use a hashmap to store the indices of the elements in the inorder list, we can reduce the time complexity to O(n), as the index lookup will take O(1) time.
