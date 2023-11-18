x=0
y=0
ans=0

def UP():
    global y
    y+=1
def DOWN():
    global y
    y+=-1
def RIGHT():
    global x
    x+=1
def LEFT():
    global x
    x+=-1    
def DISTANCE(a,b):
    return (abs(a)+abs(b))

moves=[]
print("Enter The Moves For the Bot")
while True:
    command=input()
    command=command.upper()
    moves.append(command)
    if(command=="STOP"):
        break

if(moves[0]=="START"):
    for i in moves:
        if(i!="START") and (i!="STOP"):
            globals()[i]()
        elif(i=="STOP"):
            ans=DISTANCE(x,y)

print("The Manhattan Distance of the Bot Form the Origin is",ans)