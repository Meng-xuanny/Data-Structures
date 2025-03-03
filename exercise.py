# def main():
#     my_array = [10, 20, 30, 40, 50]
#     for i in range(len(my_array)):
#         print(my_array[i], end=" ")
#
#
# main()
#
# unit_name = "ST2"

# tax = 0.177777
# print(f"The tax is {tax:.2%}")


# class Test:
#     @staticmethod
#     def main():
#         try:
#             a = 0
#             print("a =", a)
#             b = 20 / a
#             print("b =", b)
#         except ZeroDivisionError:
#             print("Divide by zero error")
#         finally:
#             print("inside the finally block")
#
# # Running the main method
# if __name__ == "__main__":
#     Test.main()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def fun1(head):
    if head is None:
        return

    fun1(head.next)
    print(head.data, end='  ')

# Example of usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Calling the function
    fun1(head)



# def fun(n):
#     if n == 4:
#         return n
#     else:
#         return 2 * fun(n + 1)
#
# if __name__ == "__main__":
#     print(fun(2))