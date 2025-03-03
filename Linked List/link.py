class Link:
    def __init__(self, datum, next=None):
        self._data=datum
        self._next=next

    def getData(self):
        return self._data

    def setData(self, data):
        self._data=data

    def getNext(self):
        return self._next

    def setNext(self, link):
        self._next = link

    def isLast(self):
        return self.getNext() is None

    def __str__(self):
        return str(self.getData())



