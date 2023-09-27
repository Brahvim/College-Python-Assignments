from numbers import Number

print("Welcome to the arithmetic operations program!")
print("This specific implementation is an interactive calculator.")
print("Try entering expressions like `1234 + 5678`! (With the spaces!):")

while True:
    print("> ", end="")

    user_input = input()
    tokens = user_input.split(" ")

    if (len(tokens)) != 3:
        print("That's not valid input!")
        continue

    a, b = tokens[0], tokens[2]

    if not (a.isdigit() or b.isdigit()):
        print("Sorry - numbers only!")
        continue

    a, b = float(a), float(b)

    result = "Oops! Looks like we can't calculate that!"

    operators = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b,
        "%": a % b,
        "^": a**b,
        "//": a // b,
    }  # ...An entire LANGUAGE to do that!

    operators["**"] = operators["^"]

    try:
        op = operators[tokens[1]]
        result = op  # (a, b)
        rounded = int(result)

        if result == rounded:
            result = rounded
    except KeyError:
        pass

    print(result)
