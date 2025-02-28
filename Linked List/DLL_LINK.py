class Link:
    def __init__(self, datum, next=None, previous=None):
        self._data = datum
        self._next = next
        self._previous = previous

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def getNext(self):
        return self._next

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self._next = link

    def getPrevious(self):
        return self._previous

    def setPrevious(self, link):
        if link is None or isinstance(link, Link):
            self._previous = link

    def isLast(self):
        return self.getNext() is None

    def isFirst(self):
        return self.getPrevious() is None

    def __str__(self):
        return str(self.getData())
