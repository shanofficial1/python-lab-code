text=input("Enter the alphanumeric : ")
uppercase=""
special=""
numbers=""
converted=""
for c in text:
    if c.isupper():
        uppercase+=c
        converted+=c.lower()
    if c.isdigit():
        numbers+=c
        converted+=c
    if not c.isalnum():
        special+=c
        converted+=c
    if c.islower():
        converted+=c.upper()
print("Uppercase letter are :",uppercase)
print("Special characters are :",special)
print("Numerels are :",numbers)
print("Converted string :",converted)
        
