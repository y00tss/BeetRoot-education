class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Invalid worker instance!")

    def get_workers(self):
        if len(self._workers) == 0:
            return f"Boss {self.name} have no workers"
        else:
            print(f"Boss {self.name} have in operation following staff: ")
            return "\n".join([f"ID: {worker.id}, Name: {worker.name}" for worker in self._workers])



class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss.get_workers().remove(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Invalid boss instance!")

# boss
boss1 = Boss(21, "John", "Apple")
boss2 = Boss(5, "Mark", "Samsung")

# creating of workers and assigning them to bosses
worker1 = Worker(5244, "Yura", "Apple", boss1)
worker2 = Worker(5245, "Vasya", "Apple", boss1)

# show all workers of boss1
print(boss1.get_workers())

# show all workers of boss2
print(boss2.get_workers())



