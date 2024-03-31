class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of the node in the tree

class AVLTree:
    def __init__(self):
        self.root = None  # Initialize root of the AVL tree to None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height  # Return the height of the node

    def getBalance(self, node):
        if not node:
            return 0
        # Calculate the balance factor of the node
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, z):
        # Right rotation operation
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateLeft(self, z):
        # Left rotation operation
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        # Insert the key recursively
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the current node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Check balance factor and perform rotations if necessary
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)

        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def insertKey(self, key):
        self.root = self.insert(self.root, key)

    def preorderTraversal(self, root):
        # Preorder traversal of the tree
        if root:
            print("{0} ".format(root.key), end="")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

# Example usage:
avl = AVLTree()
avl.insertKey(10)
avl.insertKey(20)
avl.insertKey(30)
avl.insertKey(40)
avl.insertKey(50)
avl.insertKey(25)

avl.preorderTraversal(avl.root)
