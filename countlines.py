with open("test1.txt") as f:
    line=0
    while True:
        if f.readline() != "":
            line+=1
        else:
            break
    print("Number of lines in this file is",line)
