from numbers import Number

# region Operations.
# Finally, a place for me to use lambdas (and maps)!:
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
    "^": lambda a, b: a**b,
    "//": lambda a, b: a // b,
}  # ...not just a *place*, but an entire LANGUAGE to do that!

# This allows for the use of different symbols for the 'power' operation.
operators["**"] = operators["^"]
# endregion

print("Welcome to the interactive calculator!")
print("Send in a `SIGKILL` using `^C` to exit.")
print("Try entering expressions like `1234 + 5678` (with the spaces)!:")

# TODO: Add loops to allow users to enter expressions without spaces!

while True:
    print("> ", end="")

    try:
        a, op_iden, b = input().split(" ")
    except (ValueError, IndexError):
        # `except ValueError | IndexError:` does work, but the former is better.
        print("That's not valid input!")
        continue

    try:
        a, b = float(a), float(b)
    except ValueError:
        print("Sorry - numbers only!")
        continue

    result = "Oops, I can't calculate that!"

    try:
        result = operators[op_iden](a, b)
        rounded = int(result)

        if result == rounded:
            result = rounded
    except KeyError:
        pass

    print(result)
