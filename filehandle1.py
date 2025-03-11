'''
op = input("Enter the operation (c for create, r for read, w for overwrite, a for append): ")
if op == 'c':
    name = input("Enter your name: ")
    file_name = name+".txt"
    f = open(file_name, "w")
    mail = input("Enter your email id: ")
    phone = input("Enter your phone: ")
    f.write(name + "\n")
    f.write(mail + "\n")
    f.write(phone + "\n")
    f.close()
elif op == 'r':
    name = input("Enter your name: ")
    file_name = name + ".txt"
    f = open(file_name, "r")
    print(f.read())
elif op == 'a':
    name = input("Enter your name: ")
    file_name = name + ".txt"
    f = open(file_name, "a")
    n = input("Enter your string: ")
    f.write(n + "\n")
    f.close()
elif op == 'w':
    name = input("Enter your name: ")
    file_name = name + ".txt"
    f = open(file_name, "w")
    n = input("Enter your string: ")
    f.write(n + "\n")
    f.close()
else:
    print("Invalid operation!!!")
'''

#using loop

while True:
    op = input("Enter the operation (c for create, r for read, w for overwrite, a for append, or exit): ")
    if op == 'c':
        name = input("Enter your name: ")
        file_name = name + ".txt"
        f = open(file_name, "w")
        mail = input("Enter your email id: ")
        phone = input("Enter your phone: ")
        f.write(name + "\n" + mail + "\n" + phone + "\n")
        f.close()
    elif op == 'r':
        name = input("Enter your name: ")
        file_name = name + ".txt"
        f = open(file_name, "r")
        print(f.read())
    elif op == 'a':
        name = input("Enter your name: ")
        file_name = name + ".txt"
        f = open(file_name, "a")
        n = input("Enter your string: ")
        f.write(n + "\n")
        f.close()
    elif op == 'w':
        name = input("Enter your name: ")
        file_name = name + ".txt"
        f = open(file_name, "w")
        n = input("Enter your string: ")
        f.write(n + "\n")
        f.close()
    elif op == 'exit':
        break
    else:
        print("Invalid operation!!!")