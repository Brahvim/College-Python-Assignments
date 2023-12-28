print("Python can easily do the four basic arithmetic operations, like other programming languages:")

print("`5` + `3` = ", 5 + 3)
print("`5` - `3` = ", 5 - 3)
print("`5` * `3` = ", 5 * 3)
print("`5` / `3` = ", 5 / 3)
# ^^^ This one results in a floating-point value.

print("Python has two more operators to assist in rounded-off division and exponentiation.")

print("Enter a number to try exponentiation with (enter a base): ", end="")
base = int(input())
print("Enter an exponent (Python can handle numbers with any number of digits!): ", end="")
power = int(input())
print("That'll be: ", base ** power) # Can be `^`! Yay!...

print(f"Here's the result of the computation `5 // 3`, which performs rounded division: `{5 // 3}`.")

print(f"There is support for complex numbers. Here's `(2 + 5j)` + `(9j)`: `{(2 + 5j) + (9j)}`.")

print("There is also, support for bitwise operations:")
print(0x01 | 0x00)
print(0x01 & 0x00)
print(0x01 ^ 0x00)

print("There is also string repetition ")
print("Bye" + ("e" * 105) + "!")
