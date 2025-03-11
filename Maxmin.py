# to find the maximum and minimum of two numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a > b:
    print(f"{a} is maximum and {b} is minimum")
elif a == b:
    print("Both values are equal")
else:
    print(f"{b} is maximum and {a} is minimum")
