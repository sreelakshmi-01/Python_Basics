# Take integer input till the user enters 0 and print the largest of all numbers
a = []
while True:
    b = int(input())
    if b == 0:
        break
    else:
        a.append(b)
print("Integers are: ", a)
print(max(a))
