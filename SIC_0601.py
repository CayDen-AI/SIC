## string function
def string_function():
    print("HELLO! HOW ARE YOU?".lower())
    print("this is a warning!".upper())
    x = "Once uppon a time, there was a prince and a princess.".split(" ")
    print(x)
    print(" ".join(x))
    print(len(x))
    print(x.count('a'))
    print(x[0:10])


## regex
def regex():
    import re

    x1 = "ct"
    x2 = "cat"
    x3 = "caat"
    my_expression = re.compile("c.t")
    if my_expression.search(x1):
        print("Yes!")
    else:
        print("No")

    my_exp = "ca?t"
    if re.search(my_exp, x1):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x2):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x3):
        print("Yes!")
    else:
        print("No")


    x1 = "ct"
    x2 = "cat"
    x3 = "caat"
    x4 = "caaat"

    my_exp = "ca{1,2}t"
    if re.search(my_exp, x1):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x2):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x3):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x4):
        print("Yes!")
    else:
        print("No")


    x1 = "That is your book."
    x2 = "This is my book."

    my_exp = "^This"
    if re.search(my_exp, x1):
        print("Yes!")
    else:
        print("No")

    if re.search(my_exp, x2):
        print("Yes!")
    else:
        print("No")


regex()