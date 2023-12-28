print("Enter three numbers and I will compare them for you!")

print("Enter the first one: ", end= "")
a = float(input())

print("Enter the second one: ", end= "")
b = float(input())

print("Enter the third one: ", end= "")
c = float(input())

greatest = a if a > b else b if b > a else c if c > a else a
print(f"The greatest number is...!: `{greatest}`!")
