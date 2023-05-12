def make_operation(act, *args):
    if act == '+':
        result = sum(args)
    elif act == '-':
        result = args[0] - sum(args[1:])
    elif act == '*':
        result = 1
        for num in args:
            result *= num
    return result

print("Result of first operation -", make_operation('+', 7, 7, 2))
print("Result of second operation -", make_operation('-', 5, 5, -10, -20))
print("Result of third operation -", make_operation('*', 7, 6))
