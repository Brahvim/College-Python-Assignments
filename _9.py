print("Enter a number and I'll tell you its reverse, and the sum of all of its digits.")

uin = float(input())
rev = 0
op = uin
sum = 0

while(op != 0):
    digit = op % 10
    rev = rev * 10 + digit
    sum += digit
    op //= 10

print(f"Sum of digits: `{sum}`. Digits in reverse: `{rev}`.")
