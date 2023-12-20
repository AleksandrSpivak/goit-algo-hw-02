from collections import deque


d = deque()
palindrom = True
user_input = input("Please, input a string for a check\n")

if len(user_input):
    for c in user_input:
        if c != " ":
            d.append(c.lower())

    while len(d) > 1:
        if d.pop() != d.popleft():
            palindrom = False
            break

    if palindrom:
        print(f"{user_input} is a palindrom")
    else:
        print(f"{user_input} is not a palindrom")

else:
    print("It is an empty string")
