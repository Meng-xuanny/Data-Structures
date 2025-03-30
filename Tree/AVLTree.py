class AVL_Tree:
    class _Node:
        def __init__(self, key, data):
            self.key, self.data = key, data
            self.left = self.right = None
            self.height = 1

        def updateHeight(self):
            self.height = max(
                self.left.height if self.left else 0,
                self.right.height if self.right else 0
            ) + 1

        def heightDiff(self):
            left = self.left.height if self.left else 0
            right = self.right.height if self.right else 0
            return left - right

    def __init__(self):
        self.root = None

    def rotateLeft(self, top):
        toRaise = top.right
        top.right = toRaise.left
        toRaise.left = top
        top.updateHeight()
        toRaise.updateHeight()
        return toRaise

    def rotateRight(self, top):
        toRaise = top.left
        top.left = toRaise.right
        toRaise.right = top
        top.updateHeight()
        toRaise.updateHeight()
        return toRaise

    def _insert(self, node, key, data):
        if node is None:  # base case
            return self._Node(key, data)

        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            node.data = data
            return node

        node.updateHeight()
        balance = node.heightDiff()

        if balance > 1:  # left heavy
            if key < node.left.key:  # left-left heavy
                return self.rotateRight(node)
            else:  # left-right heavy
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)

        if balance < -1:  # right heavy
            if key > node.right.key:  # right-right heavy
                return self.rotateLeft(node)
            else:  # right-left heavy
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)

        return node

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)  # returns the new root of the subtree
        # and update self.root to point to the new root

    def _minimum(self, node):
        """Find the node with the minimum key in the subtree rooted at node."""
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        if not node:
            return node  # Key not found, return unchanged

        # Step 1: Perform standard BST deletion
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: get the inorder successor (smallest in right subtree)
            successor = self._minimum(node.right)
            node.key, node.data = successor.key, successor.data
            node.right = self._delete(node.right, successor.key)  # Delete successor

        # Step 2: Update height
        node.updateHeight()

        # Step 3: Check balance factor and re-balance if needed
        balance = node.heightDiff()

        # Left Heavy (Right Rotation Needed)
        if balance > 1:
            if node.left.heightDiff() < 0:  # Left-Right Case
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        # Right Heavy (Left Rotation Needed)
        if balance < -1:
            if node.right.heightDiff() > 0:  # Right-Left Case
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node  # return the updated node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # Return the node if found, or None if not found

        if key < node.key:
            return self._search(node.left, key)  # Search in the left subtree
        else:
            return self._search(node.right, key)  # Search in the right subtree

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(f"Key: {node.key}, Data: {node.data}, Height: {node.height}")
            self.inorder_traversal(node.right)

    def print_tree(self):
        self.inorder_traversal(self.root)


# Test the AVL tree
avl = AVL_Tree()
values = [(10, "A"), (20, "B"), (30, "C"), (40, "D"), (50, "E"), (25, "F")]
for key, data in values:
    avl.insert(key, data)

avl.print_tree()
print()
avl.delete(20)
avl.print_tree()

found_node = avl.search(20)
if found_node:
    print(f"Key: {found_node.key}, Data: {found_node.data}")  # Output: Key: 20, Data: B
else:
    print("Key not found!")
