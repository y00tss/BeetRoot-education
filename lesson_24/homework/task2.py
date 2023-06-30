class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __hash_function(self, key):
        return hash(key) % self.size

    def __contains__(self, key):
        hash_value = self.__hash_function(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)
        return count

    def add(self, key, value):
        hash_value = self.__hash_function(key)
        for index, item in enumerate(self.table[hash_value]):
            if item[0] == key:
                self.table[hash_value][index] = (key, value)
                return
        self.table[hash_value].append((key, value))

    def get(self, key):
        hash_value = self.__hash_function(key)
        for item in self.table[hash_value]:
            if item[0] == key:
                return item[1]
        raise KeyError(f"{key} not found")

    def remove(self, key):
        hash_value = self.__hash_function(key)
        for index, item in enumerate(self.table[hash_value]):
            if item[0] == key:
                del self.table[hash_value][index]
                return
        raise KeyError(f"{key} not found")


hash_table = HashTable()
hash_table.add("apple", 1)
hash_table.add("banana", 2)
hash_table.add("orange", 3)

print("apple" in hash_table)  # True
print("grape" in hash_table)  # False
print(len(hash_table))        # 3
