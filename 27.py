import re

# Regular expressions
userid_re = r'^[A-Z][A-Za-z0-9@_-]{0,7}$'
password_re = r'^[A-Z](?=[A-Za-z@_-]*\d[A-Za-z@_-]*$)[A-Za-z0-9@_-]{0,7}$'

# User ID check
userid = input("Enter User ID: ")
if re.match(userid_re, userid):
    print("User ID is valid")
else:
    print("User ID is invalid")

# Password check
password = input("Enter Password: ")
if re.match(password_re, password):
    print("Password is valid")
else:
    print("Password is invalid")
