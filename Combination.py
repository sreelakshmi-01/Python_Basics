# to find the combination of 2 numbers
def fact(n):
    while n > 0:
        if n == 1:
            return 1
        else:
            return n*fact(n-1)


N = int(input("Enter the value of n: "))
R = int(input("Enter the value of r: "))

print("The combination", N, "C", R, "=", fact(N)/(fact(R)*fact(N-R)))
