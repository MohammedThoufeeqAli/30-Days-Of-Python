year=int(input("Enter the Year : "))
a=year%100
if(a==0) and (year>99):
    print("The given Year is a Century Year")
else:
    print("The given Year is Not a Century Year")