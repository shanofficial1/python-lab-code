import re

text = input("Enter the sentence: ")
pattern = input("Enter word to be searched: ")
replace = input("Enter the word to be replaced: ")

# Case-insensitive search + replacement
new_text = re.sub(pattern, replace, text, flags=re.IGNORECASE)

print("\nOriginal text:")
print(text)

print("\nAfter replacement:")
print(new_text)
