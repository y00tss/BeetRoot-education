class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, index=None):
        if self.is_empty():
            raise IndexError("pop from an empty list")

        if index is None:
            index = self.size() - 1

        if index < 0 or index >= self.size():
            raise IndexError("pop index out of range")

        if index == 0:
            data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            data = current.next.data
            current.next = current.next.next
        return data

    def insert(self, index, item):
        if index < 0 or index > self.size():
            raise IndexError("insert index out of range")

        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start >= self.size() or stop > self.size() or start >= stop:
            raise ValueError("Invalid slice parameters")

        new_list = UnorderedList()
        current = self.head
        for i in range(start):
            current = current.next

        for i in range(start, stop):
            new_list.append(current.data)
            current = current.next

        return new_list

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

# Example Usage
if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    my_list.display()  # Output: [1, 2, 3, 4, 5]

    print(my_list.index(3))  # Output: 2

    my_list.pop()      # Output: 5
    my_list.display()  # Output: [1, 2, 3, 4]

    my_list.insert(1, 6)
    my_list.display()  # Output: [1, 6, 2, 3, 4]

    new_list = my_list.slice(1, 4)
    new_list.display() # Output: [6, 2, 3]
