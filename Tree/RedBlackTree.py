
class RedBlackTree:
    class _Node:
        RED = True
        BLACK = False

        def __init__(self, key, data, color=RED):
            self.key = key
            self.data = data
            self.color = color
            self.leftChild = None
            self.rightChild = None
            self.parent = None

        def __str__(self):
            return f'{{{self.key}, {self.data}, {"R" if self.color else "B"}}}'

    def __init__(self):
        self._root = None

    def _rotate_left(self, node):
        right = node.rightChild
        node.rightChild = right.leftChild
        if right.leftChild:  # if no right
            right.leftChild.parent = node
        right.parent = node.parent
        if not node.parent:  # if node is root
            self._root = right
        elif node == node.parent.leftChild:
            node.parent.leftChild = right
        else:
            node.parent.rightChild = right
        right.leftChild = node
        node.parent = right

    def _rotate_right(self, node):
        left = node.leftChild
        node.leftChild = left.rightChild
        if left.rightChild:
            left.rightChild.parent = node
        left.parent = node.parent
        if not node.parent:
            self._root = left
        elif node == node.parent.rightChild:
            node.parent.rightChild = left
        else:
            node.parent.leftChild = left
        left.rightChild = node
        node.parent = left

    def _fix_insertion(self, node):
        while node != self._root and node.parent.color == self._Node.RED:
            if node.parent == node.parent.parent.leftChild:
                uncle = node.parent.parent.rightChild
                if uncle and uncle.color == self._Node.RED:
                    node.parent.color = self._Node.BLACK
                    uncle.color = self._Node.BLACK
                    node.parent.parent.color = self._Node.RED
                    node = node.parent.parent  # moving up the tree
                else:
                    if node == node.parent.rightChild:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = self._Node.BLACK
                    node.parent.parent.color = self._Node.RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.leftChild
                if uncle and uncle.color == self._Node.RED:
                    node.parent.color = self._Node.BLACK
                    uncle.color = self._Node.BLACK
                    node.parent.parent.color = self._Node.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.leftChild:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = self._Node.BLACK
                    node.parent.parent.color = self._Node.RED
                    self._rotate_left(node.parent.parent)
        self._root.color = self._Node.BLACK

    def insert(self, key, data):
        new_node = self._Node(key, data)
        if not self._root:
            self._root = new_node
            self._root.color = self._Node.BLACK
            return
        current = self._root
        parent = None
        while current:
            parent = current
            if key < current.key:
                current = current.leftChild
            else:
                current = current.rightChild
        new_node.parent = parent
        if key < parent.key:
            parent.leftChild = new_node
        else:
            parent.rightChild = new_node
        self._fix_insertion(new_node)  # recursively fix the colors

    def _transplant(self, u, v):
        """Replace node u with node v in the tree."""
        if u.parent is None:
            self._root = v
        elif u == u.parent.leftChild:
            u.parent.leftChild = v
        else:
            u.parent.rightChild = v
        if v:
            v.parent = u.parent

    def _minimum(self, node):
        """Find the node with the minimum key in the subtree rooted at node."""
        while node.leftChild:
            node = node.leftChild
        return node

    def delete(self, key):
        node = self._root

        # Step 1: Find the node to delete
        while node and node.key != key:
            if key < node.key:
                node = node.leftChild
            else:
                node = node.rightChild

        if node is None:
            print("Key not found")
            return

        # Step 2: Node has two children
        if node.leftChild and node.rightChild:
            successor = self._minimum(node.rightChild)
            # Copy successor's data into the node
            node.key = successor.key
            node.data = successor.data
            # Now delete the successor (which will have at most one child)
            node = successor

        # Step 3: Node has one or no children
        replacement = node.leftChild if node.leftChild else node.rightChild

        # Step 4: Transplant the replacement
        if replacement:
            self._transplant(node, replacement)
        elif node == self._root:
            self._root = None
        else:
            if node == node.parent.leftChild:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None

        # Step 5: Fix colors if needed
        if node.color == self._Node.BLACK and replacement:
            self._fix_delete(replacement)

    def _fix_delete(self, x):
        while x != self._root and x.color == 'BLACK':
            if x == x.parent.leftChild:
                sibling = x.parent.rightChild
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._rotate_left(x.parent)
                    sibling = x.parent.rightChild
                if sibling.leftChild.color == 'BLACK' and sibling.rightChild.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.rightChild.color == 'BLACK':
                        sibling.leftChild.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_right(sibling)
                        sibling = x.parent.rightChild
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.rightChild.color = 'BLACK'
                    self._rotate_left(x.parent)
                    x = self._root
            else:
                sibling = x.parent.leftChild
                if sibling.color == 'RED':
                    sibling.color = 'BLACK'
                    x.parent.color = 'RED'
                    self._rotate_right(x.parent)
                    sibling = x.parent.leftChild
                if sibling.rightChild.color == 'BLACK' and sibling.leftChild.color == 'BLACK':
                    sibling.color = 'RED'
                    x = x.parent
                else:
                    if sibling.leftChild.color == 'BLACK':
                        sibling.rightChild.color = 'BLACK'
                        sibling.color = 'RED'
                        self._rotate_left(sibling)
                        sibling = x.parent.leftChild
                    sibling.color = x.parent.color
                    x.parent.color = 'BLACK'
                    sibling.leftChild.color = 'BLACK'
                    self._rotate_right(x.parent)
                    x = self._root
        x.color = 'BLACK'

    def inOrderPrint(self, cur):
        if cur:
            self.inOrderPrint(cur.leftChild)
            print(cur, end=" ")
            self.inOrderPrint(cur.rightChild)


# Example usage:
rbt = RedBlackTree()
rbt.insert(10, 'Data 10')
rbt.insert(5, 'Data 5')
rbt.insert(15, 'Data 15')
rbt.insert(3, 'Data 3')
rbt.insert(7, 'Data 7')
rbt.insert(12, 'Data 12')
rbt.insert(18, 'Data 18')

print("In-Order Traversal:")
rbt.inOrderPrint(rbt._root)
print()
rbt.delete(5)
print(rbt._root)
rbt.inOrderPrint(rbt._root)
