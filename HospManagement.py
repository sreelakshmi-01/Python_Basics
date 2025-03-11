# to create a hospital management file handling program
import os

user = input("Enter N for new user and O for existing user: ")
new_id = 0
if user == 'N':
    while True:
        new_id += 1
        filename = str(new_id)+".txt"
        if not os.path.exists(filename):
            break
    f = open(filename, "w")
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    address = input("Enter the address: ")
    phone = int(input("Enter the phone number: "))
    f.write(str(new_id) + "\n" + name + "\n" + str(age) + "\n" + address + "\n" + str(phone) + "\n")
    f.close()
    print("Your user id = ",new_id)
    while True:
        ch = input("Choose operation (P for prescription or exit): ")
        if ch == 'P':
            f = open(filename, "a")
            pres = input("Enter the prescription: ")
            f.write(pres + "\n")
            f.close()
        elif ch == 'exit':
            break
        else:
            print("Invalid operation")
elif user == 'O':
    user_id = int(input("Enter user id: "))
    filename = str(user_id)+".txt"
    if not os.path.exists(filename):
        print("User ID not existing!!")
    else:
        f = open(filename, "r")
    while True:
        ch = input("Choose operation (P for prescription, R for read or exit): ")
        if ch == 'P':
            f = open(filename, "a")
            pres = input("Enter the prescription: ")
            f.write(pres + "\n")
            f.close()
        elif ch == 'R':
            f = open(filename, "r")
            print(f.read())
        elif ch == 'exit':
            break
        else:
            print("Invalid operation")
