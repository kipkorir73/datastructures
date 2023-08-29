class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expression):
    stack = Stack()
    open_brackets = "([{"
    close_brackets = ")]}"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty() or stack.pop() != bracket_pairs[char]:
                return False

    return stack.is_empty()
