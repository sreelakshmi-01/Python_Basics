# Calculator

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
sign = input("Enter the sign: ")

if sign == '+':
    print(a + b)
elif sign == '-':
    print(a - b)
elif sign == '*':
    print(a * b)
elif sign == '/':
    print(a / b)
else:
    print("Invalid Sign")
