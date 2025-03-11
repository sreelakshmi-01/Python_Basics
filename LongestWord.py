# To find the longest word in the sentence

a = input("Enter the sentence: ")
b = a.split()
temp = 0

for i in b:
    c = len(i)
    if c > temp:
        temp = c

for i in b:
    if len(i) == temp:
        print(i)

'''
print(max(b, key = len))
'''