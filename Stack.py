class Stack:

    def __init__(self):
        self.lst = []

    def push(self, element: object) -> object:
        self.lst.append(element)

    def pop(self, ):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.lst.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self.lst[-1]

    def is_empty(self):
        return len(self.lst) == 0





