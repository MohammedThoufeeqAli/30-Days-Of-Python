a=int(input("Enter the Positive Number a : "))
b=int(input("Enter the Another Positive Number b : "))
sum=0
if(a and b != 0):
    for i in range(1000,2001):
        if((i%a==0) and (i%b==0)):
            sum +=i        
print(sum)