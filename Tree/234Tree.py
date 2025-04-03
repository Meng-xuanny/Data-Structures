class Node:
    def __init__(self):
        self.keys = []  # Store keys in sorted order
        self.children = []  # Store child nodes

    def is_leaf(self):
        return len(self.children) == 0

    def is_full(self):
        return len(self.keys) == 3  # 4-node contains 3 keys


class Tree234:
    def __init__(self):
        self.root = Node()

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:   # Find the correct position in the node
            return True  # Key found
        elif node.is_leaf():
            return False  # If the key is not found and the node is a leaf
        else:
            return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if root.is_full():  # Split root if full
            new_root = Node()
            new_root.children.append(self.root)
            self.split_node(new_root, 0)  # Split old root
            self.root = new_root  # New root
        self._insert_non_full(self.root, key)

    def split_node(self, parent, index):
        node = parent.children[index]  # Get the full 4-node that needs splitting
        mid_key = node.keys[1]  # Extract the middle key

        # Create a new node and move the largest key from the original node to it
        new_node = Node()
        new_node.keys.append(node.keys.pop(2))  # Move the largest key to the new node

        # If the node is not a leaf, transfer its children
        if not node.is_leaf():
            new_node.children.append(node.children.pop(2))
            new_node.children.append(node.children.pop(2) if len(node.children) > 2 else None)

        # Move the middle key up to the parent node
        parent.keys.insert(index, mid_key)

        # Add the new node as the parent's child
        parent.children.insert(index + 1, new_node)

    def _insert_non_full(self, node, key):
        if node.is_leaf():
            node.keys.append(key)
            node.keys.sort()  # Maintain order
        else:  # If the Node is Internal → Find the Correct Child to Insert Into
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if node.children[i].is_full():
                self.split_node(node, i)
                if key > node.keys[i]:  # decide again which subtree key should go into
                    i += 1
            self._insert_non_full(node.children[i], key)


# Example Usage:
tree = Tree234()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
print(tree.search(30))  # Output: True
print(tree.search(50))  # Output: False

