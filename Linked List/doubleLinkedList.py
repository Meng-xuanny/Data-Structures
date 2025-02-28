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
            if self._first:  # If the list is not empty
                link.setNext(self._first)  # New first node points to the old first
                self._first.setPrevious(link)  # Old first node points back to the new first
            self._first = link
            if self.getLast() is None:  # Only reset _last if the list is empty
                self._last = link  #update both ends so that when a node is inserted, it is both the last and first
        else:
            raise Exception("First link must be Link or None.")

    def setLast(self, link):
        if link is None or isinstance(link, Link):
            if self._last:  # If the list is not empty
                link.setPrevious(self.getLast())  # New last node points to the old last
                self._last.setNext(link)
            self._last = link
            if self.getFirst() is None:
                self._first = link
        else:
            raise Exception("First link must be Link or None.")

    def insertFirst(self, datum):
        link = Link(datum, next=self.getFirst())
        if self.isEmpty():
            self.setFirst(link)
        else:
            self.getFirst().setPrevious(link)
            self.setFirst(link)

    insert = insertFirst  #overwrite insert()

    def insertLast(self, datum):
        link = Link(datum, previous=self.getLast())
        if self.isEmpty():
            self.setLast(link)
        else:
            self.getLast().setNext(link)
            self.setLast(link)  #Always update _last

    def delete(self, goal, key=lambda x: x):
        """Deletes a node with the given key."""
        if self.isEmpty():
            return Exception("Cannot delete from empty list.")

        target_node = self.find(goal, key)
        if not target_node:
            return False  # Key not found

        if target_node == self.getFirst():
            self._first = target_node.getNext()
            if self._first:
                self._first.setPrevious(None)

        elif target_node == self.getLast():  # If deleting tail
            self._last = target_node.getPrevious()
            if self._last:
                self._last.setNext(None)

        else:  # If deleting a middle node
            target_node.getPrevious().setNext(target_node.getNext())
            target_node.getNext().setPrevious(target_node.getPrevious())

        return target_node.getData()

    def traverse_forward(self):
        """Prints the list from head to tail."""
        current = self._first
        while current:
            print(current.getData(), end=" <-> ")
            current = current.getNext()
        print("None")

    def traverse_backward(self):
        """Prints the list from tail to head."""
        current = self._last
        while current:
            print(current.getData(), end=" <-> ")
            current = current.getPrevious()
        print("None")


ddl = DoublyLinkedList()
ddl.insert(None)
ddl.insertLast("c")
ddl.setFirst(Link(0))
ddl.insert("b")
print(ddl)

ddl.setLast(Link("e"))
print(ddl)
# print(ddl.delete("c"))
ddl.delete("b")
ddl.delete("e")
print(ddl)

ddl.traverse_forward()
ddl.traverse_backward()
