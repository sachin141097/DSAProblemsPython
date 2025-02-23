class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree_from_inorder_and_preorder(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])
    root.left = construct_binary_tree_from_inorder_and_preorder(
        preorder[1 : root_index + 1], inorder[:root_index]
    )
    root.right = construct_binary_tree_from_inorder_and_preorder(
        preorder[root_index + 1 :], inorder[root_index + 1 :]
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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = construct_binary_tree_from_inorder_and_preorder(preorder, inorder)
    print(f"Level order traversal of the constructed tree is: {levelorder(root)}")
