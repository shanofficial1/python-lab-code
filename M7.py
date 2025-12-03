l1=[1,2,3,4,5,6,7]
l2=[8,9,9,7]

def com(l1,l2):
    for i in l1:
        for j in l2:
            if j==i:
                print("Common element is ",i)
                return True
    return False

if com(l1,l2):
    print("It has common atleast one element")
else:
    print("No common element")

    
        
