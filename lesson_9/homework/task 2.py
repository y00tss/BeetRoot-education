while True:
    try:
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        print((number1**2) / number2)
        break
    except ZeroDivisionError:
        print("Cant be divided to 0! Try again.")
        continue
    except ValueError:
        print("Seems, that was entered word... Try again.")
        continue