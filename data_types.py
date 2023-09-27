def wait_for_read(s):
    print("\n\n(Please press `Enter` to continue the program.)")
    input()
    print(s)


# The assignment *itself* asks for a resource to be copied.
# Find it here!: https://www.vogella.com/tutorials/Python/article.html

###################################################
print("Type checking with `type()` and `isinstance()`:")

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is complex number?", isinstance(a, complex))

###################################################
wait_for_read("Python integers (`int`s):")

a = 12
print(type(a))
b = 456792357968700
print(b)
print(type(b))

###################################################
wait_for_read("Python `float`s:")

f = 3.413
print(f)
print(type(f))
f1 = 1.2e4
print(f1)

###################################################
wait_for_read("The Python `complex` data type:")

c = 3 + 4j
print(type(c))
print(c.real)
print(c.imag)

###################################################
wait_for_read("Python `bool`s:")

b = True
print(type(b))
a = 5
b = 8
c = a < b
print(c)

###################################################
wait_for_read("Python `long`s (which are just `int`s!):")

a = 1234567890123456789
print(a)

b = 0.1234567890123456789
print(b)  # Value of 'b' is truncated!

c = 1 + 2j
print(c)

###################################################
wait_for_read("Python (text) strings:")

s = "This is a string"
print(s)
s = """A 
multiline 
string"""
print(s)


# Throws a `SyntaxError`!:

# input()
# print("Python can also throw syntax errors!")

# s = "python
# is a
# freeware"
# print(s)
