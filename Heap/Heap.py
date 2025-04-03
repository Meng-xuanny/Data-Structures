class Heap:
    def __init__(self, key=lambda x: x, size=2):
        self._arr = [None] * size
        self._nItems = 0
        self._key = key

    def isEmpty(self):
        return self._nItems == 0

    def isFull(self):
        return self._nItems == len(self._arr)

    def __len__(self):
        return self._nItems

    def peek(self):
        return None if self.isEmpty() else self._arr[0]

    # return the parent index
    def parent(self, i):
        return (i - 1) // 2

    # return left child's index
    def leftChild(self, i):
        return i * 2 + 1

    # return right child's index
    def rightChild(self, i):
        return i * 2 + 2

    def insert(self, item):
        if self.isFull():
            self._growHeap()
        self._arr[self._nItems] = item
        self._nItems += 1
        self._siftUp(self._nItems - 1)  # sift up the last element

    def _growHeap(self):
        current = self._arr
        self._arr = [None] * max(1, 2 * len(self._arr))
        for i in range(self._nItems):
            self._arr[i] = current[i]

    def _siftUp(self, i):
        if i <= 0: return  # can't go higher than root
        parent = self.parent(i)  # parent's index
        if self._key(self._arr[i]) > self._key(self._arr[parent]):
            self._swap(parent, i)
            self._siftUp(parent)

    def _swap(self, i, j):
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    # remove top item and return it
    def remove(self):
        if self.isEmpty():
            raise Exception("Heap underflow")
        root = self._arr[0]
        self._arr[0] = self._arr[self._nItems - 1]  # move the last element to root
        self._arr[self._nItems - 1] = None  # clear the last element
        self._nItems -= 1
        self._siftDown(0)
        return root

    def _siftDown(self, i):
        left, right = self.leftChild(i), self.rightChild(i)
        largest = i  # Assume the current node is the largest

        # Check if left child exists and is larger than the current node
        if left < self._nItems and self._key(self._arr[left]) > self._key(self._arr[largest]):
            largest = left

        # Check if right child exists and is larger than the current largest node
        if right < self._nItems and self._key(self._arr[right]) > self._key(self._arr[largest]):
            largest = right

        # If the largest value is not the current node, swap and recurse
        if largest != i:
            self._swap(i, largest)
            self._siftDown(largest)  # Continue sifting down

        return    # If i is already the largest node in the heap

    def printHeap(self):
        if self.isEmpty():
            print("Heap is empty.")
            return
        print("Heap elements:", [self._arr[i] for i in range(self._nItems)])


def heapSort(arr):
    n = len(arr)
    # Step 1: Build Max Heap (Heapify each non-leaf node from bottom up)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element with last element
        _heapify(arr, i, 0)  # Heapify the reduced heap. The parameter i determines the new size of the heap

    return arr


def _heapify(arr, n, i):
    largest = i  # Assume current node is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


# Example Usage
arr = [4, 10, 3, 5, 1]
sorted_arr = heapSort(arr)
print(sorted_arr)  # Output: [1, 3, 4, 5, 10]

heap = Heap()
heap.insert(30)
heap.insert(20)
heap.insert(25)
heap.insert(5)
heap.insert(10)
heap.insert(40)
heap.printHeap()
heap.remove()
heap.printHeap()

