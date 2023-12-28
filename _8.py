print("Enter two numbers and I'll tell you which one is larger.")

print("Enter one of 'em: ", end="")
a = float(input())

print("Enter the other: ", end="")
b = float(input())

print(f"`{a if a > b else b}` is the largest number you entered!")
