import identity


class Queue:
    def __init__(self, size):
        self._maxSize=size
        self._que = [None] * size
        self._front=0
        self._rear=-1
        self._nItems=0

    def isFull(self):
        if self._nItems == self._maxSize:
            return True

    def isEmpty(self):
        return self._nItems == 0

    def insert(self,item):
        if self.isFull():
            raise Exception("Queue overflow")

        self._rear = (self._rear +1 ) % self._maxSize
        self._que[self._rear]=item
        self._nItems += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self._que[self._front]
        self._que[self._front] = None
        self._front = (self._front + 1) % self._maxSize  # Wrap around
        self._nItems -= 1
        return front

    def __str__(self):
        return str(self._que[:self._nItems])


queue = Queue(5)
queue.insert(20)
queue.insert(30)
queue.insert(40)
queue.insert(50)
print(queue)
print(queue.remove())



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
        j=self._nItems -1
        while j >=0 and (self._pri(item) >= self._pri(self._que[j])):
            self._que[j+1]=self._que[j] #moving the item to the front
            j-=1
        self._que[j+1]=item
        self._nItems+=1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        self._nItems-=1
        front = self._que[self._nItems] # #least value first out (end of queue)
        self._que[self._nItems]=None
        return front

    def __str__(self):
        return str(self._que[:self._nItems])

priQueue=PriorityQueue(3)
priQueue.insert(10)
priQueue.insert(30)
priQueue.insert(20)
print(priQueue)
print(priQueue.remove())