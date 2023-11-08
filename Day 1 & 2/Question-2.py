words=[]
for i in range(0,5):
    a=input("Enter the Word : ") 
    words.append(a) 
print("")    
for i in range(0,5):
    if(i!=4):
        print(words[i],end=" ") 
    else:
        print(words[i]+".")