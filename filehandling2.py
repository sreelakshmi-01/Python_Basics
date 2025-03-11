n = int(input("Enter the count: "))
for i in range(1, n+1):
    f = open("new.txt", "a")
    a = int(input())
    a = str(a)
    f.write(a + "\n")
    f.close()

