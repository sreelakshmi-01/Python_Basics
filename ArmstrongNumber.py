# To check for Armstrong Number

a = int(input("Enter a number: ")) #153
sum = 0
b = int(len(str(a)))
temp = a

while temp > 0:
    digit = temp % 10 # 153 % 10 = 3 || 15 % 10 = 5 || 1 % 10 = 1
    sum += digit ** b # sum+= 3**3 = 27 || 27 + 5**3 = 152 || 152 + 1**3 = 153
    temp //= 10 # 153 // 10 = 15 || 15 // 10 = 1 || 1 // 10 = 0 (out of loop with aum 153)

if sum == a: #(153 = 153)
    print("Armstrong Number!!")
else:
    print("Not an Armstrong Number")
