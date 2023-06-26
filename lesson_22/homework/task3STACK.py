class Stack:
    def __init__(self, word):
        self.word = word
        self.stack = []  # Merhaba

    def create_stack(self):
        for item in self.word:
            self.stack.append(item)

    def delete_element(self, element):
        if element in self.stack:
            self.stack.remove(element)
        elif len(self.stack) == 0:
            print("Stack is empty")
        else:
            raise ValueError("Element not found")

    def search_element(self, element):
        if element in self.stack:
            print(element)
        elif len(self.stack) == 0:
            print("Stack is empty")
        else:
            raise ValueError("Element not found")

    def get_stack(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print(*self.stack)


a = Stack("Misha")
a.create_stack()
print('!!!printing stack!!!')
a.get_stack()

print('-' * 20)
print('!!!deleting element!!!')
a.delete_element('a')
print('!!!printing stack result!!!')
a.get_stack()

print('-' * 20)
print('!!!searching element!!!')
a.search_element('M')
a.get_stack()

