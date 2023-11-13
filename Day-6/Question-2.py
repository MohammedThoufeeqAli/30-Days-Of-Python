num=int(input("Enter the Positive Number : "))
for i in range(1,num+1):
    if(i!=num):
        print(i,end=",")    
    else:
        print(i,".",sep="")    