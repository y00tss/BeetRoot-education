import collections


class Queue:
    def __init__(self, word):
        self.word = word
        self.queue = collections.deque()

    def create_queue(self):
        for item in self.word:
            self.queue.append(item)

    def delete_element(self, element):
        if element in self.queue:
            self.queue.remove(element)
        elif len(self.queue) == 0:
            print("Queue is empty")
        else:
            raise ValueError("Element not found")

    def search_element(self, element):
        if element in self.queue:
            print(element)
        elif len(self.queue) == 0:
            print("Queue is empty")
        else:
            raise ValueError("Element not found")

    def get_queue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print(*self.queue)

b = Queue("Vika")
b.create_queue()
print('!!!printing queue!!!')
b.get_queue()

print('-' * 20)
print('!!!deleting element!!!')
b.delete_element('a')
print('!!!printing queue result!!!')
b.get_queue()

print('-' * 20)
print('!!!searching element!!!')
b.search_element('i')
b.get_queue()








