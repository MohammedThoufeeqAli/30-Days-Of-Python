string1=input("Enter the String : ")
string2=string1.lower()
string2=sorted(string2) 
print("Sorted String is ",end="")
for i in string2:
    print(i,end="")