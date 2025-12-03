import re

password = input("Enter password: ")

if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
    print("✅ Contains both lowercase and uppercase letters")
else:
    print("❌ Must contain at least one lowercase and one uppercase letter")
