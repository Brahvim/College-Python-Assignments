from numbers import Number

# region Operators.
# Finally! A place for me to use lambdas:
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
    "^": lambda a, b: a**b,
    "//": lambda a, b: a // b,
}  # ...An entire LANGUAGE to do that!

# We need dis!!!:
operators["**"] = operators["^"]
# endregion


print("Welcome to the arithmetic operations program!")
print("This specific implementation is an interactive calculator.")
print("Try entering expressions like `1234 + 5678`! (With the spaces!):")

while True:
    print("> ", end="")

    user_input = input()
    tokens = user_input.split(" ")
    num_tokens = len(tokens)

    if num_tokens != 3:
        print("That's not valid input!")
        continue

    a = tokens[0]
    b = tokens[2]

    if not (a.isdigit() or b.isdigit()):
        print("Sorry - numbers only!")
        continue

    a = float(a)
    b = float(b)

    result = "Oops! Looks like we can't calculate that!"

    try:
        op = operators[tokens[1]]
        result = op(a, b)
        rounded = int(result)

        if result == rounded:
            result = rounded
    except KeyError:
        pass

    print(result)
