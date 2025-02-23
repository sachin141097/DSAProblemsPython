"""
This script defines a binary tree and provides various methods to manipulate and traverse the tree.

Classes:
- Node: Represents a node in the binary tree.
- Tree: Represents the binary tree and contains methods for insertion, traversal, and calculating the maximum depth.

Methods:
- insert: Inserts a new node with the given key into the binary tree.
- preorder: Performs a preorder traversal of the binary tree.
- inorder: Performs an inorder traversal of the binary tree.
- postorder: Performs a postorder traversal of the binary tree.
- levelorder: Performs a level order traversal of the binary tree.
- max_depth: Calculates the maximum depth of the binary tree using recursion.
- max_depth_using_level_order: Calculates the maximum depth of the binary tree using level order traversal.

Approach:
1. The `insert` method inserts a new node into the binary tree. If the tree is empty, the new node becomes the root. Otherwise, the method recursively finds the correct position for the new node based on its value.
2. The `preorder`, `inorder`, and `postorder` methods perform their respective tree traversals using recursion.
3. The `levelorder` method performs a level order traversal using a queue. It processes each level of the tree one by one and appends the values of the nodes at each level to the result list.
4. The `max_depth` method calculates the maximum depth of the tree using recursion. It finds the maximum depth of the left and right subtrees and returns the greater of the two depths plus one.
5. The `max_depth_using_level_order` method calculates the maximum depth of the tree using level order traversal. It processes each level of the tree and increments the depth counter for each level.

Time Complexity:
- The `insert` method has a time complexity of O(h), where h is the height of the tree.
- The `preorder`, `inorder`, and `postorder` methods have a time complexity of O(n), where n is the number of nodes in the tree.
- The `levelorder` method has a time complexity of O(n), where n is the number of nodes in the tree.
- The `max_depth` method has a time complexity of O(n), where n is the number of nodes in the tree.
- The `max_depth_using_level_order` method has a time complexity of O(n), where n is the number of nodes in the tree.
"""


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
