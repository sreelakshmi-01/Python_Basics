# Take integer input till the user enters 0 and print the sum of all numbers
a = []
while True:
    b = int(input())
    if b == 0:
        break
    else:
        a.append(b)
print("Integers are: ", a)

sum = 0
for i in a:
    sum += i
print("The sum is ", sum)
