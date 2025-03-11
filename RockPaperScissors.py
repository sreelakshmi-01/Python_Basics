# Rock Paper Scissors
import random

print("1. Rock \n2.Paper \n3. Scissors \n")


def sys_choice():
    if r == 1:
        print("System choice: Rock")
    elif r == 2:
        print("System choice: Paper")
    else:
        print("System choice: Scissors")


def user_choice():
    if choice == 1:
        print("\nYour choice: Rock")
    elif choice == 2:
        print("\nYour choice: Paper")
    else:
        print("\nYour choice: Scissors")


user_count = 0
sys_count = 0
for i in range(1, 6):
    choice = int(input("\nEnter your choice: "))
    r = random.randint(1, 3)

    if choice == r:
        user_choice()
        sys_choice()
    elif (choice == 1 and r == 3) or (choice == 2 and r == 1) or (choice == 3 and r == 2):
        user_choice()
        sys_choice()
        user_count += 1
    elif (choice == 1 and r == 2) or (choice == 2 and r == 3) or (choice == 3 and r == 1):
        user_choice()
        sys_choice()
        sys_count += 1
    else:
        print("Invalid choice!!!")
        break

print("\nYour Score: ", user_count)
print("System Score: ", sys_count)

if user_count > sys_count:
    print("\nYou won!!!")
elif user_count == sys_count:
    print("\nDraw!!")
else:
    print("\nYou lose!!!!")
