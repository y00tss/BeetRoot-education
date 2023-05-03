# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

# getting example
user_answer = input("Enter an example: ")

# Secondary Operations
string_len = len(user_answer)

# Main operation
if string_len >= 2:
    sl1 = user_answer[:2]
    sl2 = user_answer[-2:]
    result = sl1 + sl2
    print(result)
else:
    print("Empty String")
