import identity


class Queue:
    def __init__(self, size):
        self._maxSize = size
        self._que = [None] * size
        self._front = 1
        self._rear = 0
        self._nItems = 0

    def isFull(self):
        return self._nItems == self._maxSize

    def isEmpty(self):
        return self._nItems == 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")

        self._rear = (self._rear + 1) % self._maxSize
        self._que[self._rear] = item
        self._nItems += 1

    #for dequeue
    def insertFront(self, item):
        if self.isFull():
            raise Exception("Dequeue overflow")

        if self.isEmpty():
            self.insert(item)
        else:
            self._front = (self._front - 1) % self._maxSize  # Move front backward

        self._que[self._front] = item
        self._nItems += 1

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self._que[self._front]
        self._que[self._front] = None
        self._front = (self._front + 1) % self._maxSize  # Wrap around
        self._nItems -= 1
        return front

    #for dequeue
    def removeRear(self):
        if self.isEmpty():
            raise Exception("Dequeue underflow")

        item = self._que[self._rear]
        self._que[self._rear] = None
        self._rear = (self._rear - 1) % self._maxSize  # Move rear backward
        self._nItems -= 1

        return item


    def __str__(self):
        if self.isEmpty():
            return "[]"

        result = []
        index = self._front
        for _ in range(self._nItems):
            result.append(str(self._que[index]))
            index = (index + 1) % self._maxSize  # Move forward circularly

        return "[" + ", ".join(result) + "]"


# queue = Queue(5)
# queue.insert(20)
# queue.insert(30)
# queue.insert(50)
# queue.insertFront(2)
# print(queue)
# print(queue.remove())
# print(queue.removeRear())
# print(queue)


class PriorityQueue:
    def __init__(self, size, pri=lambda x: x):
        self._maxSize = size
        self._que = [None] * size
        self._pri = pri
        self._nItems = 0

    def isFull(self):
        if self._nItems == self._maxSize:
            return True

    def isEmpty(self):
        return self._nItems == 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        j = self._nItems - 1
        while j >= 0 and (self._pri(item) >= self._pri(self._que[j])):
            self._que[j + 1] = self._que[j]  #moving the item to the front
            j -= 1
        self._que[j + 1] = item
        self._nItems += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self._que[self._nItems - 1]   #least value first out (end of queue)
        self._que[self._nItems - 1] = None
        self._nItems -= 1
        return front

    def __str__(self):
        return str(self._que[:self._nItems])

# priQueue = PriorityQueue(3)
# priQueue.insert(10)
# priQueue.insert(30)
# priQueue.insert(20)
# print(priQueue)
# print(priQueue.remove())
# print(priQueue)
