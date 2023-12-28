print("Enter a number to check if it is a prime: ", end="")
uin = int(input())

is_prime = False
for i in range(uin + 1):
    mod_result = i % uin
    if mod_result == int(mod_result):
        is_prime = True

print("That seems to be a prime!" if is_prime else "That isn't a prime.")
