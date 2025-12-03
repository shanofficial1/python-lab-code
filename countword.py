with open("test.txt") as f:
     content=f.read();
     words=content.split()
     print("NUMBER OF WORDS IN THIS FILE IS",len(words))
