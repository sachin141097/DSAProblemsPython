class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    queue = []
    if not root:
        return []
    queue.append(root)
    result = []
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(node.val)
    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(f"Right side view of the binary tree: {right_side_view(root)}")
