a = int(input("Enter the length of list: "))
b = []

for i in range(a):
    c = int(input("Enter element: "))
    b.append(c)
    i += 1
    
print(b)

b.sort()
print(f"Sorted list: {b}")
print(f"Min: {b[0]}")
print(f"Max: {b[-1]}")
