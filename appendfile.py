with open("secondfile.txt") as f1:
    file1=f1.read()
    print("Second file: \n",file1)
    with open("firstfile.txt","r+") as f2:
        file3=f2.read()
        print("First file : \n",file3)
        f2.write("\n")
        f2.write(file1)
with open("firstfile.txt") as f3:
    file4=f3.read()
    print("After append first file : \n",file4)
        
        
