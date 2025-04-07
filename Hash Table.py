# --- Helper Functions ---
def simpleHash(key):
    if not isinstance(key, str):
        key = str(key)
    a = 33
    hash_val = 0
    # spread out the hash value
    for c in key:
        hash_val = hash_val * a + ord(c)  # ord(c) gives the ASCII (or Unicode) value of the character c
    return hash_val


def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class KeyValueList:
    def __init__(self):
        self.head = None

    # insert in the front
    def insert_key(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return False  # key updated, not added
            current = current.next
        # Create a new node if the key was not found
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        return True

    def search_key(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def traverse(self):
        current = self.head
        items = []
        while current:
            items.append((current.key, current.value))
            current = current.next
        return items

    def delete_key(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False  # Key not found


# --- Hash Table Class ---
class HashTable():
    def __init__(self, size=7, hash=simpleHash, maxLoadFactor=1.0):
        self.__table = [None] * size
        self.__nItems = 0
        self.__hash = hash
        self.__maxLoadFactor = maxLoadFactor

    def __len__(self):
        return self.__nItems

    def cells(self):
        return len(self.__table)

    def hash(self, key):
        return self.__hash(key) % self.cells()

    def insert(self, key, value):
        i = self.hash(key)
        if self.__table[i] is None:
            self.__table[i] = KeyValueList()
        flag = self.__table[i].insert_key(key, value)   # return False if the key already exists,
        # or True if it was successfully inserted.
        if flag:
            self.__nItems += 1
            # Check if the load factor exceeds the maximum load factor
            if self.loadFactor() > self.__maxLoadFactor:
                self.__growTable()
        return flag  # indicator

    def loadFactor(self):  # the ratio of the number of items in the table to the number of cells
        return self.__nItems / self.cells()

    def __growTable(self):
        oldTable = self.__table
        size = len(oldTable) * 2 + 1
        while not is_prime(size):
            size += 2
        self.__table = [None] * size
        self.__nItems = 0
        # Re-insert all the existing key-value pairs from the old table into the new table
        for bucket in oldTable:
            if bucket:
                for key, value in bucket.traverse():
                    self.insert(key, value)

    def search(self, key):
        i = self.hash(key)
        return None if self.__table[i] is None else self.__table[i].search_key(key)

    def delete(self, key):
        i = self.hash(key)
        if self.__table[i] is None:
            return False  # Key doesn't exist

        deleted = self.__table[i].delete_key(key)
        if deleted:
            self.__nItems -= 1
            return True
        return False

    def __str__(self):
        result = []
        for idx, cell in enumerate(self.__table):
            if cell is None:
                result.append(f"[{idx}] -> Empty")
            else:
                pairs = ", ".join(f"{k}: {v}" for k, v in cell.traverse())
                result.append(f"[{idx}] -> {pairs}")
        return "\n".join(result)


# --- Test the HashTable ---
if __name__ == "__main__":
    ht = HashTable(size=5, maxLoadFactor=0.75)
    ht.insert("apple", 5)
    ht.insert("banana", 10)
    ht.insert("grape", 20)
    print(ht)
    ht.insert("orange", 15)  # trigger grow
    ht.insert("kiwi", 25)
    ht.delete("apple")

    print("Current Hash Table:")
    print(ht)

    print("\nSearching:")
    print("grape:", ht.search("grape"))
    print("mango:", ht.search("mango"))  # should return None
