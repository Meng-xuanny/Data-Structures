from link import Link

class LinkedList:
    def __init__(self):
        self._first = None

    def isEmpty(self):
        return self.getFirst() is None

    def getFirst(self):
        return self._first

    def setFirst(self, link):
        self._first=link

    def insert(self, datum): # insert a link at the start of the linkedList
        link = Link(datum, self.getFirst())
        self.setFirst(link)

    def insertAfter(self, goal, datum, key=lambda x: x): #insert after a link with a certain key
        link = self.find(goal,key)
        if link is None: return False
        newLink = Link(datum, link.getNext())
        link.setNext(newLink)
        return True

    def find(self, goal, key=lambda x: x):
        link=self.getFirst() #start from the first link
        while link is not None:
            if key(link.getData()) == goal:
                return link
            link= link.getNext() # to next link

    def delete(self, goal,key=lambda x: x ):
        if self.isEmpty():
            raise Exception("Cannot delete from empty list.")
        # deleting the first link
        if key(self.getFirst().getData()) == goal:
            self.setFirst(self.getFirst().getNext())
            return True
        # If the goal is in any other position, find the previous link
        link = self.getFirst()
        while link.getNext() is not None:
            if key(link.getNext().getData()) == goal:
                link.setNext(link.getNext().getNext())
                return True
            link = link.getNext()
        return False #the goal was not found


    def __str__(self):
        result="["
        link=self.getFirst()
        while link is not None:
            if len(result) >1:
                result+=">"
            result+=str(link)
            link=link.getNext()
        return result + "]"


# linked= LinkedList()
# linked.insert(1)
# linked.insert(2)
# linked.insert(3)
# linked.insert(4)
# print(linked)
# print(linked.find(3))
# linked.insertAfter(4, "a")
# print(linked)
# print(linked.delete(0))