# To check if word is palindrome
a = input("Enter a word: ")
if a == a[::-1]:
    print("Palindrome!!")
else:
    print("Not Palindrome...")
