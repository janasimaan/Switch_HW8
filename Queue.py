class Queue:
    def __init__(self):
        self.lst=[]

    def enqueue(self, element):
        self.lst.append(element)

    def dequeue(self):
        if self.is_empty:
            raise Exception("Queue is empty")
        return self.lst.pop(0)

    def peek(self):
        if self.is_empty:
            raise Exception("Queue is empty")
        return self.lst[0]

    def is_empty(self):
        return len(self.lst) == 0

