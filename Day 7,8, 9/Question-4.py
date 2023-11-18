num=input("Enter the Phone Number : ")
num_list=[]
length=len(num)
temp1=0
temp2=1
temp3=0

for i in num:
    num_list.append(i)

for i in num_list:
    b=num_list.count(i)
    if(b>7):
        temp1=1

for i in range(length-1):
    if(num_list[i]==num_list[(i+1)%length]):
        temp2=temp2+1
    else:
        if(temp2>temp3):
            temp3=temp2
        temp2=1       

if (num_list[0] =='6') or(num_list[0] =='7') or (num_list[0] =='8') or (num_list[0] =='9'):
    if(len(num_list)==10):
        if(temp1!=1):
            if(temp3<=5):
                print("Valid Number")
            else:
                print("Invalid Number")    
        else:
            print("Invalid Number")    
    else:
        print("Invalid Number")    
else:
    print("Invalid Number")    