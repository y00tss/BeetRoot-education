class Mathematician:
    pass

    def square_nums(self, list_of_nums):
        return [x ** 2 for x in list_of_nums]

    def remove_positives(selfself, list_of_numbers):
        return [x for x in list_of_numbers if x <= 0]

    def filter_leaps(self, list_of_numbers):
        return [x for x in list_of_numbers if x % 4 == 0]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]



print("-" * 100)
# to ensure


print(m.square_nums([7, 11, 5, 4]))

print(m.remove_positives([26, -11, -8, 13, -90]))

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
