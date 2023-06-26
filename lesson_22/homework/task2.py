s = input("Enter a string: ")

stack = []
flag = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif i in ")]}":
        if not stack:
            flag = False
            break
        result = stack.pop()
        if result == '(' and i == ')':
            continue
        elif result == '[' and i == ']':
            continue
        elif result == '{' and i == '}':
            continue
        else:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

# quick examples
# (M[e[r]h]a)(b[a]){} - YES
# (M[e[r(h]a)(b[a]){} - NO
