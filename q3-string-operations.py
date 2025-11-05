s=list(input("Enter a string: "))
ulist=[]
slist=[]
nlist=[]
for i in range(len(s)):
    if s[i].isupper():
        ulist.append(s[i])
        print("Changed", s[i], "to", s[i].lower())
        s[i] = s[i].lower()
    if not s[i].isalnum() and not s[i].isspace():
        slist.append(s[i])
    if s[i].isnumeric():
        nlist.append(s[i])
    
        
print("Modified string:","".join(s))
print("Uppercase letters:","".join(ulist))
print("Special characters:","".join(slist))
print("Numbers:","".join(nlist))