emp=[]
temp=0

for i in range(0,5):
    a=int(input("Enter the Employee Id : ")) 
    emp.append(a)
    
for o in range(0,5):
    if(o!=4):
        if((emp[o]+emp[o+1])%2==0):
            temp=1
        else:
            temp=0   
    else:
        if((emp[o]+emp[0])%2==0):
            temp=1
        else:
            temp=0   

if(temp==1):
    print("\nYes the Meeting will be Conducted")
else:
    print("\nNo the Meeting will not be Conducted")   