from Stack import *

def reverse_books(book_ids):
    stack = Stack()
    for _ in book_ids:
        stack.push(_)

    new_stack = []
    while not stack.is_empty():
        new_stack.append(stack.pop())

    return new_stack


print(reverse_books([101, 102, 103, 104]))
print(reverse_books([1, 2, 3]))
print(reverse_books([]))
print(reverse_books([42]))
