"""stack = []


def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False


def push(n):
    stack.append(n)


def pop():
    if not is_empty():
        stack.pop()


push(4)
print(stack)

a = is_empty()
print(a)"""


from collections import deque


def push(stack, item):
    new_stack = deque(stack)
    new_stack.append(item)
    return new_stack


