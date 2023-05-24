import time


def add_func(first, second):
    time.sleep(3)
    print("Now I inside second function... Calculation...")
    result = first + second
    return result


def main(first, second):
    print("Now Im working inside firs func, but Im going to next func")
    result_of_func = add_func(first, second)
    time.sleep(3)
    print("I got the result in the second function and returned to the first")
    print(f"{first} + {second} = {result_of_func}")


main(int(input("Enter first digit: ")), int(input("Enter second digit: ")))
