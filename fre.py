with open("freq.txt") as f:
    content=f.read()
    words=content.split( )
    fr={}
    for i in words:
        if i in fr:
            fr[i]+=1
        else:
            fr[i]=1
for key,value in fr.items():
    print(key ,":",value)
            
