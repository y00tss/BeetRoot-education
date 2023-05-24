import random

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def check_minus(spisok):
    flag = True
    for value in range(len(spisok)):
        if spisok[value] < 0:
            flag = False
            return flag
    return flag


def choose_func(spisok):
    if check_minus(spisok):
        return square_nums(spisok)
    else:
        return remove_negatives(spisok)


assert choose_func(nums1) == [1, 4, 9, 16, 25]
assert choose_func(nums2) == [1, 3, 5]
print("Any AssertionError. ANd printing results: ")
print(choose_func(nums1))
print(choose_func(nums2))