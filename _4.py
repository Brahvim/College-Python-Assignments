print("Enter the number to be checked for Armstrong number behavior: ", end="")

num = int(input())
op = num
sum = 0

while(op != 0):
    digit = op % 10
    digit_cubed = digit ** 3
    sum +=  digit_cubed
    op //= 10

print("That is an Armstrong number!" if sum == num else "That isn't an Armstrong number.")
