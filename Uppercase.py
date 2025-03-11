#Uppercae first nd last letters of  word (Word must contain at least 4 letters)

a = input("Enter a word: ")
if len(a) < 4:
    print("Enter a word containing at least 4 letters!!")
else:
    b = list(a)
    b[0] = b[0].upper()
    b[-1] = b[-1].upper()
    c = ''.join(b)
    print(c)
