with open("test.txt") as f:
    l=list(f.read())
    a=0
    n=0
    s=0
    for i in l:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            n+=1
        else:
            s+=1
    print("Alphabets :",a)
    print("\n Numerics :",n)
    print("\n Special Character :",s)
