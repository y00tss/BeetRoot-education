class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop.")

        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek.")
        return self.head.data

    def show(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements


stack = Stack()

# Pushing elements into the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Showing the current state of the stack
print("Stack elements:", stack.show())

# Peeking the top element
print("Top element:", stack.peek())

# Popping elements from the stack
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

# Showing the current state of the stack after popping elements
print("Stack elements:", stack.show())
