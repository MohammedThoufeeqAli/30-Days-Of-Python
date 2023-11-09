a=int(input("Enter the length of the 1st side : "))
b=int(input("Enter the length of the 2nd side : "))
c=int(input("Enter the length of the 3rd side : "))

if(a==b==c):
    print("It is a Equilateral Triangle")
elif(a==b)or(b==c)or(a==c):
    print("It is a Isosceles Triangle")
else:
    print("It is a Scalene Triangle")