s = input("Enter an alphanumeric string: ")

uppercase = ""
special = ""
numbers = ""
converted = ""

for ch in s:
    # i. Uppercase letters
    if ch.isupper():
        uppercase += ch

    # iii. Numerals
    if ch.isdigit():
        numbers += ch

    # ii. Special characters
    if not ch.isalnum():
        special += ch

    # iv. Case conversion
    if ch.isupper():
        converted += ch.lower()
    elif ch.islower():
        converted += ch.upper()
    else:
        converted += ch

print("Uppercase letters:", uppercase)
print("Special characters:", special)
print("Numerals:", numbers)
print("After case conversion:", converted)
