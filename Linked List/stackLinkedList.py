from Stack.stack import Stack
from link import Link



class StackLinkedList:
    def __init__(self, max_size):
        self.stack = Stack(max_size)

    def isEmpty(self):
        return self.stack.isEmpty()

    def push(self, datum):  # Insert at the start (like insertFirst)
        link = Link(datum, self.stack.peek())
        self.stack.push(link)

    def pop(self):  # Delete from the start (like deleteFirst)
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):  # Get the first element (like getFirst)
        return self.stack.peek()

    def insertLast(self, datum):
        if self.isEmpty():
            self.push(datum)
            return

        temp_stack = Stack(self.stack._maxSize)
        while not self.stack.isEmpty():
            temp_stack.push(self.stack.pop())

        new_link = Link(datum)
        if not temp_stack.isEmpty():
            temp_stack.peek().setNext(new_link)
        temp_stack.push(new_link)

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

    def deleteLast(self):
        if self.isEmpty():
            return None
        if self.stack._top == 0:  # Only one element
            return self.pop()

        temp_stack = Stack(self.stack._maxSize)
        while self.stack._top > 0:
            temp_stack.push(self.stack.pop())

        deleted = self.stack.pop()  # Last element
        if not temp_stack.isEmpty():
            temp_stack.peek().setNext(None)

        while not temp_stack.isEmpty():
            self.stack.push(temp_stack.pop())

        return deleted

    def __str__(self):
        result = "["
        for i in range(self.stack._top + 1):
            if i > 0:
                result += ">"
            result += str(self.stack._s[i])
        return result + "]"




linked= StackLinkedList(5)
linked.push(1)
linked.push(2)
linked.push(3)
linked.push(4)
print(linked)
print(linked.peek())
linked.insertLast("a")
print(linked)
print(linked.pop())
print(linked.deleteLast())
print(linked)