time=int(input("Enter the Hour of the Day(0-23) : "))
if (time<0) or (time>23):
    print("\nINVALID")
else:
    if(0<=time<=5):
        print("\nIt's NIGHT Time")
    elif(6<=time<=11):
        print("\nIt's MORNING Time")    
    elif(12<=time<=17):
        print("\nIt's AFTERNOON Time")
    elif(18<=time<=23):
        print("\nIt's EVENING Time")