import os

filename = input("Enter file name: ")

try:
    # Check if file already exists
    if os.path.exists(filename):
        print("File already exists. Cannot open in write mode.")
    else:
        file = open(filename, "w")
        print("File opened successfully in write mode.")
        file.write("This file is created using exception handling.\n")
        file.close()

except IOError:
    print("Error while opening the file.")
