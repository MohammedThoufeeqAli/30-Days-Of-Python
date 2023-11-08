a=int(input("Enter the First Number : ")) 
b=int(input("Enter the Second Number : "))
print("\nBefore Swapping :") 
print("First Number : "+str(a)+", Second Number : "+str(b))
a=a+b
b=a-b
a=a-b
print("\nAfter Swapping :") 
print("First Number : "+str(a)+", Second Number : "+str(b))
