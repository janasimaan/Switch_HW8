from Queue import *
from Stack import *

def brackets_valid(s):
    stack = Stack()
    dict = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in dict:
            top_element = stack.pop()
            if top_element != dict[char]:
                return False
        else:
            stack.push(char)
    return stack.is_empty()

print(brackets_valid("()"))
print(brackets_valid("()[]{}"))
print(brackets_valid("(]"))
print(brackets_valid("([)]"))
print(brackets_valid("{[]}"))
print(brackets_valid(""))