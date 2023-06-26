def reverce(word):
    stack = []

    for item in word:
        stack.append(item)

    avoid_stopping = list(stack)

    for item in stack:
        print(avoid_stopping.pop(), end=" ")


reverce(input("Enter word: "))
