class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def show(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Test the implementation
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.show()                                # Output: 1 -> 2 -> 3 -> 4 -> None

    print("Front of the queue:", queue.peek())  # Output: Front of the queue: 1

    print("Dequeue:", queue.dequeue())          # Output: Dequeue: 1

    queue.show()                                # Output: 2 -> 3 -> 4 -> None

    print("Front of the queue:", queue.peek())  # Output: Front of the queue: 2
