class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key > root.val:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def levelorder(self, root):
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def max_depth(self, root):
        if not root:
            return 0
        else:
            left_depth = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            return max(left_depth, right_depth) + 1

    def max_depth_using_level_order(self, root):
        if not root:
            return 0
        queue = []
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


if __name__ == "__main__":
    n = int(input(f"Enter the number of nodes: "))
    print("Enter the values of the nodes: ")
    # take space separated input of the nodes
    nodes = list(map(int, input().split()))
    tree = Tree()
    for node in nodes:
        tree.root = tree.insert(tree.root, node)
    print(f"Preorder traversal of the tree is: ", end="")
    tree.preorder(tree.root)
    print()
    print(f"Inorder traversal of the tree is: ", end="")
    tree.inorder(tree.root)
    print()
    print(f"Postorder traversal of the tree is: ", end="")
    tree.postorder(tree.root)
    print()
    print(f"Level order traversal of the tree is: {tree.levelorder(tree.root)}")
    print(f"Maximum depth of the tree is: {tree.max_depth(tree.root)}")
    print(
        f"Maximum depth of the tree using level order traversal is: {tree.max_depth_using_level_order(tree.root)}"
    )
