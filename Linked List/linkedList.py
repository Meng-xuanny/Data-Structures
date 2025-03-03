from link import Link


class LinkedList:
    def __init__(self):
        self._first = None

    def isEmpty(self):
        return self.getFirst() is None

    def getFirst(self):
        return self._first

    def setFirst(self, link):
        self._first = link

    def insert(self, datum):  # insert a link at the start of the linkedList
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def insertAfter(self, goal, datum, key=lambda x: x):  #insert after a link with a certain key
        link = self.find(goal, key)
        if link is None:
            raise Exception(f"No link equal to {goal}")
        newLink = Link(datum, link.getNext())
        link.setNext(newLink)

    def insertLast(self, datum):
        if self.isEmpty():
            self.insert(datum)
        else:
            last = self.getFirst()
            while last.getNext() is not None:
                last = last.getNext()
            last.setNext(Link(datum))

    def find(self, goal, key=lambda x: x):
        link = self.getFirst()  #start from the first link
        while link is not None:
            if key(link.getData()) == goal:
                return link
            link = link.getNext()  # to next link

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Cannot delete from empty list.")
        data = self.getFirst().getData()
        self.setFirst(self.getFirst().getNext())
        return data

    # def delete(self, goal, key=lambda x: x):
    #     if self.isEmpty():
    #         raise Exception("Cannot delete from empty list.")
    #
    #     link = self.find(goal, key)
    #     if link is None:
    #         raise Exception(f"No link equal to {goal}")
    #     # deleting the first link
    #     if link == self.getFirst():
    #         return self.deleteFirst()
    #     else:
    #         data = link.getData()
    #         prev = self.getFirst() #find the previous link
    #         while prev.getNext() != link:
    #             prev=prev.getNext()
    #         prev.setNext(link.getNext())
    #         return data

    def delete(self, goal, key=lambda x: x):
        if self.isEmpty():
            raise Exception("Cannot delete from empty list.")

        prev = None
        curr = self.getFirst()

        while curr is not None:
            if key(curr.getData()) == goal:
                # If deleting the first node
                if prev is None:
                    self.deleteFirst()
                else:
                    prev.setNext(curr.getNext())  # Bypass the current node
                return curr.getData()

            prev = curr
            curr = curr.getNext()

        raise Exception(f"No link equal to {goal}")

    def deleteLast(self):
        if self.isEmpty():
            return Exception("Cannot delete from empty list.")

        if self.getFirst().getNext() is None:
            # If there's only one node, remove it
            deleted = self.getFirst()
            self.setFirst(None)
            return deleted

        # Traverse to the second-to-last node
        prev = self.getFirst()
        while prev.getNext().getNext() is not None:
            prev = prev.getNext()
        # Delete last node
        deleted = prev.getNext()
        prev.setNext(None)
        return deleted

    def recReverse(self, node):
        if node is None or node.getNext() is None:
            return node

        new_head = self.recReverse(node.getNext())
        node.getNext().setNext(node)  # Make the next node point back to the current node
        node.setNext(None)  # Break the current node's old link
        return new_head

    def reverse(self):
        self._first = self.recReverse(self._first)
        return self

    def __str__(self):
        result = "["
        link = self.getFirst()
        while link is not None:
            if len(result) > 1:
                result += ">"
            result += str(link)
            link = link.getNext()
        return result + "]"


linked = LinkedList()
linked.insert(1)
linked.insert(2)
linked.insert(3)
linked.insertLast(5)
linked.insert(4)
print(linked)
print(linked.reverse())

# # print(linked.find(3))
# # linked.insertAfter(4, "a")
# # print(linked)
# print(linked.delete(0))
# linked.deleteLast()
# print(linked)
# print(linked.deleteFirst())
