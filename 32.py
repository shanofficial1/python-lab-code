import re

text = input("Enter a string containing date: ")

# Regular expression pattern for dates (DD/MM/YYYY or DD-MM-YYYY)
pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b'

dates = re.findall(pattern, text)

if dates:
    print("Date(s) found:")
    for d in dates:
        print(d)
else:
    print("No date found.")
