import re

text = input("Enter a text: ")

# Regular expressions
uppercase = re.findall(r'[A-Z]', text)
lowercase = re.findall(r'[a-z]', text)
special = re.findall(r'[^A-Za-z0-9\s]', text)

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Special characters:", special)
