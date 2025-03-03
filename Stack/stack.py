class Stack:
    def __init__(self,max):
        self._s=[None]*max
        self._top=-1
        self._maxSize = max  # Store max size for overflow check

    def isEmpty(self):
        return self._top <0

    def isFull(self):
        """Check if the stack is full."""
        return self._top >= self._maxSize - 1

    def peek(self):
        if not self.isEmpty():
            return self._s[self._top]

    def push(self,item):
        if self.isFull():
            raise Exception("Stack overflow, cannot push.")
        self._top+=1
        self._s[self._top]=item

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow, cannot pop.")
        top =self._s[self._top]
        self._s[self._top] = None
        self._top-=1
        return top

    def __str__(self):
        return str(self._s[:self._top + 1])


# stack=Stack(4)
# stack.push(2)
# # stack.push(4)
# # stack.push(1)
# print(stack)
# print(stack.pop())
# print(stack.peek())