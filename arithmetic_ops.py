import numbers


def is_number(p_param):
    return isinstance(p_param, Number)


# def is_int(p_param):
#     return isinstance(p_param, int)


# def is_float(p_param):
#     return isinstance(p_param, float)


# def is_complex(p_param):
#     return isinstance(p_param, complex)


print("Welcome to the arithmetic operations program!")
print("This specific implementation is an interactive calculator.")
print("Try entering expressions like `1234 + 5678`.")

while True:
    print("> ", end="")

    user_input = input()
    tokens = user_input.split(" ")
    num_tokens = len(tokens)

    if num_tokens != 3:
        print("That's not valid input!")
        continue

    if not (is_number(tokens[0]) or is_number(tokens[2])):
        print("Sorry - numbers only!")
        continue

    a = tokens[0]
    b = tokens[2]
    user_op = tokens[1]
    result = "Oops! Looks like we don't calculate that!"

    if user_op == "+":
        result = a + b
    elif user_op == "-":
        result = a - b
    elif user_op == "*":
        result = a * b
    else:
        pass

    print(result)
