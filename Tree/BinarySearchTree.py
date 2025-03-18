class BinarySearchTree:
    class _Node:
        def __init__(self, key, data, left=None, right=None):
            self.key = key
            self.data = data
            self.leftChild = left
            self.rightChild = right

        def __str__(self):
            return "{" + str(self.key) + "," + str(self.data) + "}"

    def __init__(self):
        self._root = None

    def preOrderPrint(self, cur):
        if cur:
            print(" " + str(cur), end="")
            self.preOrderPrint(cur.leftChild)
            self.preOrderPrint(cur.rightChild)

    def inOrderPrint(self, cur):
        if cur:
            self.inOrderPrint(cur.leftChild)
            print(" " + str(cur), end="")
            self.inOrderPrint(cur.rightChild)

    def postOrderPrint(self, cur):
        if cur:
            self.postOrderPrint(cur.leftChild)
            self.postOrderPrint(cur.rightChild)
            print(" " + str(cur), end="")

    def _find(self, goal):
        current = self._root
        parent = self  # the BST object

        while current and goal != current.key:
            parent = current
            if goal < current.key:
                current = current.leftChild
            else:
                current = current.rightChild

        return current, parent

    def _rfind(self, goal, current="start", parent=None):
        if current == "start":
            current = self._root
            parent = self
        # base case
        if not current or goal == current.key:
            return current, parent

        if goal < current.key:
            return self._rfind(goal, current.leftChild, current)
        else:
            return self._rfind(goal, current.rightChild, current)

    def insert(self, key, data):
        node, parent = self._find(key)

        if node:  # if we find a node with this key, update the data
            node.data = data
            return False  # no insertion

        if parent is self:  # empty tree
            self._root = self._Node(key, data)
        elif key < parent.key:
            parent.leftChild = self._Node(key, data)
        else:
            parent.rightChild = self._Node(key, data)
        return True

    def delete(self, goal):
        node, parent = self._find(goal)
        if node:
            return self._delete(parent, node)
        return None

    def _delete(self, parent, node):
        deleted = node.data

        if node.leftChild and node.rightChild:
            self._promote_successor(node)
        elif node.leftChild:  # Node has only left child
            if parent is self:  # if node is root
                self._root = node.leftChild
            elif parent.leftChild is node:  # if node's parent's left
                parent.leftChild = node.leftChild  # update parent's left
            else:  # if node's parent's right
                parent.rightChild = node.leftChild
        elif node.rightChild:  # Node has only right child
            if parent is self:  # if node is root
                self._root = node.rightChild
            elif parent.leftChild is node:  # if node's parent's left
                parent.leftChild = node.rightChild  # update parent's left
            else:  # if node's parent's right
                parent.rightChild = node.rightChild
        else:  # Node has no children
            if parent is self:  # If node is root
                self._root = None
            elif parent.leftChild is node:
                parent.leftChild = None  # Update parent's left
            else:
                parent.rightChild = None  # Update parent's right

        return deleted

    def _promote_successor(self, node):  # when deleting a node with both subtree
        successor = node.rightChild
        parent = node
        while successor.leftChild:  # find the successor with no left
            parent = successor
            successor = successor.leftChild

        # Replace the node's key and data with the successor's
        node.key = successor.key
        node.data = successor.data
        # Recursively delete the successor
        self._delete(parent, successor)


def test_delete():
    tree = BinarySearchTree()

    # Insert some nodes
    tree.insert(10, 'Data 10')
    tree.insert(5, 'Data 5')
    tree.insert(15, 'Data 15')
    tree.insert(3, 'Data 3')
    tree.insert(7, 'Data 7')
    tree.insert(12, 'Data 12')
    tree.insert(18, 'Data 18')
    tree.insert(8, "Data 8")
    tree.insert(16, "Data 16")
    tree.insert(17, "Data 17")

    print(tree._root)

    # Test In-Order traversal before deletion
    print("In-Order before deletion:")
    tree.inOrderPrint(tree._root)
    print()
    #
    # # Test deleting leaf node (Node with no children)
    # print("Delete 3 (leaf node):")
    # deleted_data = tree.delete(3)
    # print(f"Deleted: {deleted_data}")
    # tree.inOrderPrint(tree._root)
    # print()
    #
    # # Test deleting node with one child
    # print("Delete 7 (node with one child):")
    # deleted_data = tree.delete(7)
    # print(f"Deleted: {deleted_data}")
    # tree.inOrderPrint(tree._root)
    # print()

    # Test deleting node with two children
    print("Delete 15 (node with two children):")
    deleted_data = tree.delete(15)
    print(f"Deleted: {deleted_data}")
    tree.inOrderPrint(tree._root)
    print()

    # # Test deleting root node
    # print("Delete 10 (root node):")
    # deleted_data = tree.delete(10)
    # print(f"Deleted: {deleted_data}")
    # tree.inOrderPrint(tree._root)
    # print()
    #
    # # Test deleting a non-existent node
    # print("Delete 100 (non-existent node):")
    # deleted_data = tree.delete(100)
    # print(f"Deleted: {deleted_data}")  # Expected: None
    # tree.inOrderPrint(tree._root)  # Expected: 7, 12, 15, 18
    # print()


test_delete()
