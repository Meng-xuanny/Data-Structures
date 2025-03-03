from Queue.queue import Queue



class QueueLinkedList:
    def __init__(self, size):
        self._deque = Queue(size)  # Use your Queue class as a deque

    def insertFirst(self, item):
        """Insert an item at the front of the linked list (O(1))."""
        self._deque.insertFront(item)

    def insertLast(self, item):
        """Insert an item at the end of the linked list (O(1))."""
        self._deque.insert(item)

    def deleteFirst(self):
        """Remove and return the first item (O(1))."""
        if self._deque.isEmpty():
            raise Exception("List is empty")
        return self._deque.remove()

    def deleteLast(self):
        """Remove and return the last item (O(1))."""
        if self._deque.isEmpty():
            raise Exception("List is empty")
        return self._deque.removeRear()

    def isEmpty(self):
        """Check if the list is empty."""
        return self._deque.isEmpty()

    def isFull(self):
        """Check if the list is full."""
        return self._deque.isFull()

    def __str__(self):
        """Return a string representation of the linked list."""
        return str([item for item in self._deque._que if item is not None])



ll = QueueLinkedList(5)
ll.insertFirst(10)
ll.insertLast(20)
ll.insertFirst(5)
ll.insertLast(30)
print(ll)
print(ll.deleteLast())
ll.deleteFirst()
print(ll)