# Open file in read mode
with open("sample.txt", "r") as file:
    content = file.read()

print("----- File content BEFORE replacement -----")
print(content)

old_word = input("Enter the word to search: ")
new_word = input("Enter the new word: ")

# Replace all occurrences
updated_content = content.replace(old_word, new_word)

# Open file in write mode to save changes
with open("sample.txt", "w") as file:
    file.write(updated_content)

print("\n----- File content AFTER replacement -----")
print(updated_content)

