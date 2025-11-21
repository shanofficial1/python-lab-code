n=int(input(("Enter the limit")))
i=1
while(i<=n):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
            if count>2:
                break
           
    if count==2:
        print(i)
    i+=1
