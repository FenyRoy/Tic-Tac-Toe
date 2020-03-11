size=0
list1=[]
def createtable(x):
    global size
    size=x
    global list1
    list1=[]
    for i in range(x):
        list1.append([])
        for j in range(x):
            list1[i].append(0)

def rowcheck():
    global list1
    for i in range(size):
        ismatch=1
        test=list1[i][0]
        if test == 0:
            ismatch=0
        for j in range(1,size):
            if test != list1[i][j]:
                ismatch=0
        if ismatch == 1:
            print("Match Won by Player: ",test)
            return 1
    return 0


def colcheck():
    global list1
    for i in range(size):
        ismatch=1
        test=list1[0][i]
        if test == 0:
            ismatch=0
        for j in range(1,size):
            if test != list1[j][i]:
                ismatch=0
        if ismatch == 1:
            print("Match Won by Player: ",test)
            return 1
    return 0

def dia1check():
    global list1
    ismatch=1
    test=list1[0][0]
    if test == 0:
        ismatch = 0
    for i in range(1,size):
        if test != list1[i][i]:
            ismatch = 0
    if ismatch == 1:
        print("Match Won by Player: ",test)
        return 1
    else:
        return 0

def dia2check():
    global list1
    ismatch=1
    test=list1[0][size-1]
    if test == 0:
            ismatch = 0
    for i in range(1,size):
        j=size-i-1
        if test != list1[i][j]:
            ismatch = 0
    if ismatch == 1:
        print("Match Won by Player: ",test)
        return 1
    else:
        return 0
    
def inputttt(s):
    a=int(input(s))
    if a <= size:
        a-=1
    else:
        a=inputtt(s)
    return a    


def play(a,b,c):
    global list1
    if list1[a][b]==0:
        list1[a][b]=c
    else:
        print("Already filled cell! \n Try Again")
        a=inputttt("Row : ")
        b=inputttt("Column : ")
        play(a,b,c)

def displayttt():
    global list1
    for i in range(size):
        print(list1[i])


def starttictactoe():
    print("Instructions: It is a two player game. Here each player will get their corresponding turns")
    x=int(input("Enter the size of table: "))
    z=input("Enter the Number of players(Default is 2): ")
    try:
       y = int(z)
    except ValueError:
       y=2
    if y<2 :
        y=2
    createtable(x)
    i=-1
    displayttt()
    while True:
        i=i+1
        i%=y
        print("Player %1d Enter the row and column: "%(i+1))
        a=inputttt("Row : ")
        b=inputttt("Column : ")
        play(a,b,i+1)
        displayttt()
        if rowcheck():
            break
        if colcheck():
            break
        if dia1check():
            break
        if dia2check():
            break
