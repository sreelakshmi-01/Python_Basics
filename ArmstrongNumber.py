# To check for Armstrong Number

a = int(input("Enter a number: "))
sum = 0
b = int(len(str(a)))
temp = a

while temp > 0:
    digit = temp % 10
    sum += digit ** b
    temp //= 10

if sum == a:
    print("Armstrong Number!!")
else:
    print("Not an Armstrong Number")
