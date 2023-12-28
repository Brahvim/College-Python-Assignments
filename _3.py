print("Enter a number or word you want checked for being a palindrome: ", end="")

uin = input()   # `uin` here, stands for
                # "**u**esr **in**put"

print("That is a palindrome!" if uin == uin[::-1] else "That is not a palindrome.")
