with open("test.txt") as f:
    l=list(f.read())
    vl=[]
    for i in l:
        if i.upper() in ["A","E","I","O","U"]:
            vl.append(i)

    print("NUMBER OF VOWELS IN THIS FILe IS",len(vl))
    
