"""
There are two kinds of loops in Python: `for` and `while`.

- `while` takes a condition and loops till it is `False`.
- `for` takes a "sequence" object, and loops till it has executed for each element.
In most languages, this is known as a for-each loop.
"""


def wait_for_read(s: str) -> str:
    print(f"\n\n(Please press `Enter` to see code output for {s}.)")
    input()


# Iterating over an array:
wait_for_read("iteration over an array")

for i in [12, 3.4, 0x56]:  # `0x56` is `86` in decimal.
    if i % 2 == 0:
        print(f"The number `{i}` is even!")
    else:
        print(f"The number `{i}` is odd.")

# Iterating over a generated range, which simulates a traditional `for` loop,
# and also provides control over the generated range:
wait_for_read("iteration using `range()` till a given `stop` value is reached")

for i in range(5):
    print(i)

wait_for_read("iteration using `range()` with a `start` and `stop` value")

for i in range(2, 5):
    print(i)

wait_for_read("iteration using `range()` with a `start`, `stop` and `step`")

print("This should print the multiplication table for `2`:", end=" ")
for i in range(0, 10, 2):
    print(
        f"`{i}`",
        # Here lies Python's ternary operator - ...which is more of a functional construct:
        end="." if i == 8 else ", ",
    )

# Iteration over a tuple:
wait_for_read("iteration using tuples")
for i in (1, 2.0, 0x03):
    print(i)

# Iteration over a set:
wait_for_read("iteration using sets")
for i in {1, 2.0, 0x03}:
    print(i)

# Iteration over a dictionary:
wait_for_read("iteration over dictionaries")

for k, v in {"A": "Apple", "B": "Ball"}.items():
    print(f"'{k}' is for \"{v}\"!")

# Using a `while` loop:
wait_for_read("demonstrating `while` loops")

x = 0

while True:
    print("Enter a non-zero real number, please?:", " ")
    uin = input()
    if uin.isnumeric():
        f = float(uin)
        x = f if f == x else int(f)
        break

print("Thanks!")

# Nesting of loops:
wait_for_read("demonstrating nested [`for`] loops")

matrix = [
    [x * i for i in range(3)],
    [x ** (i * 2) for i in range(3)],
    [x ** (i * x) for i in range(3)],
]

print("Here's a matrix of numbers generated using what you gave earlier!:")

# No, I'm not gunna find a way to format these. Let them be the way they are!:
for row in matrix:
    for n in row:
        print(n, end="  ")
    print()
