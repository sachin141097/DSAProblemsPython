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
