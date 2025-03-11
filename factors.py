#Input a number and find all factors of that number

def factor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")


n = int(input("Enter a number: "))
factor(n)
