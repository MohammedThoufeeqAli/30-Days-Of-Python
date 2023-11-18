num=int(input("Enter Positive Integer : "))
print("The Number Arrow")
for i in range(1,num+1):
    for o in range(0,i):
        if(o!=i-1):
            print(o+1,end=",")
        else:
            print(o+1)    

for i in range(num-1,0,-1):
    for o in range(0,i):
        if(o!=i-1):
            print(o+1,end=",")
        else:
            print(o+1)