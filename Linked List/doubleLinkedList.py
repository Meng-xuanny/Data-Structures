from linkedList import LinkedList
from DLL_LINK import Link


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self._first, self._last = None, None

    def getFirst(self):
        return self._first

    def getLast(self):
        return self._last

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self._first = link
            if (self._last is None or link is None):
                self._last = link  #update both ends so that when a node is inserted, it is both the last and first
        else:
            raise Exception("First link must be Link or None.")

    def setLast(self, link):
        if link is None or isinstance(link, Link):
            self._last = link
            if (self._last is None or link is None):
                self._first = link
        else:
            raise Exception("First link must be Link or None.")

    def insertFirst(self, datum):
        link = Link(datum, next=self.getFirst())
        if self.isEmpty():
            self.setLast(link)
        else:
            self.getFirst().setPrevious(link)
        self.setFirst(link)

    insert = insertFirst #overwrite insert()

    def insertLast(self, datum):
        link = Link(datum, previous=self.getLast())
        if self.isEmpty():
            self.setFirst(link)
        else:
            self.getLast().setNext(link)
        self.setLast(link)  #Always update _last

    def delete(self, goal, key=lambda x: x):
        link = self.find(goal, key)
        if link is None:
            raise Exception("Cannot find link in the list")
        if link.isLast():
            return self.deleteLast()
        elif link.isFirst():
            return self.deleteFirst()
        else:
            link.getNext().setPrevious(link.getPrevious())
            link.getPrevious().setNext(link.getNext())
            return link.getData()

    def deleteLast(self):
        if self.isEmpty():
            raise Exception("Cannot delete from an empty list.")

        data = self.getLast().getData()
        if self.getFirst() == self.getLast():  # Only one element
            self.setFirst(None)
            self.setLast(None)
        else:
            self.setLast(self.getLast().getPrevious())
            self.getLast().setNext(None)
        return data

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Cannot delete from an empty list.")

        data = self.getFirst().getData()
        if self.getFirst() == self.getLast():  # Only one element
            self.setFirst(None)
            self.setLast(None)
        else:
            self.setFirst(self.getFirst().getNext())  #update first
            self.getFirst().setPrevious(None)
        return data  # Return deleted data


ddl = DoublyLinkedList()
ddl.insert("a")
ddl.insertLast("c")
ddl.insert("b")
print(ddl)
print(ddl.delete("b"))
print(ddl)
print(ddl.deleteLast())

