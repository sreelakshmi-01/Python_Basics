text = "CS Term2 2022"
L = len(text)
new = ""
for i in range(0, L):
    if text[i].isupper():
        new=new+text[i].lower()
    elif text[i].islower():
        new=new+text[i].upper()
    else:
        new=new+"#"
print(new)