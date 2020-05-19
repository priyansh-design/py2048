import copy
import random
import os
import argparse
from pynput import keyboard
def isPowerOfTwo(x): 
	return (x and (not(x & (x - 1))) ) 


if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument("--n",help="boardsize")
	parser.add_argument("--w",help="winning tile")
	args=parser.parse_args()




	 
print("HELLO EVERYBODY,WE ARE BRINGING YOU THE GAME OF 2048")

print("ALL THE BEST,LETSSSSS BEGIN......")
v=args.w

if v.isnumeric():
        v=int(v)
        while v<2:
                v=int(input("this winning tile is not possible,enter a valid tile:"))
        if not isPowerOfTwo(v):
                v=int(input("enter a number with a power of 2:"))
  

       
else:
	print("your input is not valid,so it is set to default value 2048")
	v=2048
boardsize=args.n
if boardsize.isnumeric():
    boardsize=int(boardsize)
    while boardsize<1:
        boardsize=int(input("this boardsize is not valid,enter a boardsize greater than 1:"))
else:
	print("your input is not valid,so it is set to default value 5")
	boardsize=5
def newvalue():
    return 2
def nextnum():
    row=random.randint(0,boardsize-1)
    col=random.randint(0,boardsize-1)
    
    while not board[row][col]==0:
        row=random.randint(0,boardsize-1)
        col=random.randint(0,boardsize-1)
    board[row][col]=newvalue()    
board=[[0 for x in range(boardsize)] for y in range(boardsize)]
inival=1
row=random.randint(0,boardsize-1)
col=random.randint(0,boardsize-1)
while inival>0:
    if board[row][col]==0:
       board[row][col]=newvalue()
       inival-=1
#here is the formation of board
def display():
    l=board[0][0]
    for row in board:
        for item in row:
            if item>l:
                l=item
    maxS=len(str(l))
    for row in board:
        line='|'
        for item in row:
            if item==0:
                line+=' '*maxS+'|'
            else:
                line+=(' '*(maxS-len(str(item))))+str(item)+'|'
        print(line)
    
#here it is merging left

def tninrow(row):
    count=0
    for i in row:
        if i!=0:
            count+=1
    return count        
    
def merge1row(row):
    for j in range(tninrow(row)):
        
        for i in range(boardsize-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    
    
    for i in range(boardsize-1):
        if row[i]==row[i+1]:
            row[i]=row[i]*2
            row[i+1]=0 
    for i in range(boardsize-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0        
    return row        
def merge_left(currentboard):
    for i in range(boardsize):
        currentboard[i]=merge1row(currentboard[i])
    return currentboard
#this is merging right    
    
def reverse(row):
    revrow=[]
    for i in range(boardsize-1,-1,-1):
        revrow.append(row[i])
    return revrow 
def merge_right(currentboard):
    for i in range(boardsize):
        currentboard[i]=reverse(currentboard[i])
        currentboard[i]=merge1row(currentboard[i])
        currentboard[i]=reverse(currentboard[i])
    return currentboard 
 
def transpose(currentboard):
    temp=[[0 for x in range(boardsize)] for y in range(boardsize)]
    for i in range(boardsize):
        for j in range(boardsize):
            temp[j][i]=currentboard[i][j]
           
    return temp
#merge up
def merge_up(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_left(currentboard)
    currentboard=transpose(currentboard)
    
    return currentboard
def merge_down(currentboard):
    currentboard=transpose(currentboard)
    currentboard=merge_right(currentboard)
    currentboard=transpose(currentboard)
    
    return currentboard
#winner is declared
def won():
    for row in board:
        for item in row:
            if item==v:
                return True
    return False 
#loser is declared    
def lose():
    b1=copy.deepcopy(board)
    b2=copy.deepcopy(board)
    b1=merge_up(b1)
    if b1==b2:
        b1=merge_down(b1)
        if b1==b2:
            b1=merge_left(b1)
            if b1==b2:
                b1=merge_right(b1)
                if b1==b2:
                    return True
    return False
def ipt():
     with keyboard.Events() as events:
        event = events.get()
        if event.key == keyboard.KeyCode.from_char('w'):
            return 'w'
            
        if event.key == keyboard.KeyCode.from_char('a'):
            return 'a'
            
        if event.key == keyboard.KeyCode.from_char('s'):
            return 's'
            
        if event.key == keyboard.KeyCode.from_char('d'):
            return 'd' 
                  


try:
        if v>2 and boardsize>1:
                
                print("here is your game board:")    
                display()
              

                gameover=False
                while not gameover:
                    print("enter your move")
                    m=ipt()
                    os.system('cls')
                    correctinput=True
                    dupliboard=copy.deepcopy(board)
                    if m =="w":
                       board=merge_up(board)
                       
                        
                        
                    elif m =="s":
                       board=merge_down(board)
                       
                        
                    elif m =="a":
                       board=merge_left(board)
                       
                       
                        
                    elif m =="d":
                       board=merge_right(board)
                       
                        
                        
                    else:
                       correctinput=False

                    
                    if not correctinput:
                        print("your input was wrong,Please try again:")
                        display()
                    else:
                        if board==dupliboard:
                            print("Try in a different direction,this move does not make any change")
                            display()
                        else:
                            if won():
                                display()
                                print("volaaa...,you WON!!!")
                                
                                gameover=True
                            else:
                                nextnum()
                                display()
                                if lose():
                                    print("sorry, you lost .you dont have more steps to play")
                                    
                                    gameover=True

        elif v==2 and boardsize>1:
                v=input("with winning tile 2,game will not played further therefore enter a valid the winning tile:")

                if v.isnumeric():
                    v=int(v)
                    while v<2:
                            v=int(input("this winning tile is not possible,enter a valid tile:"))
                    if not isPowerOfTwo(v):
                            v=int(input("enter a number with a power of 2:"))
                  

                       
                else:
                    print("your input is not valid,so it is set to default value 2048")
                    v=2048           
           
                print("here is your game board:")    
                display()
                

                gameover=False
                while not gameover:
                    print("enter your move")
                    m=ipt()
                    os.system('cls')
                    correctinput=True
                    dupliboard=copy.deepcopy(board)
                    if m =="w":
                       board=merge_up(board)
                       
                        
                        
                    elif m =="s":
                       board=merge_down(board)
                       
                        
                    elif m =="a":
                       board=merge_left(board)
                       
                       
                        
                    elif m =="d":
                       board=merge_right(board)
                       
                        
                        
                    else:
                       correctinput=False
                       
                    
                    if not correctinput:
                        print("your input was wrong,Please try again:")
                        display()
                    else:
                        if board==dupliboard:
                            print("Try in a different direction,this move does not make any change")
                            display()
                        else:
                            if won():
                                display()
                                print("volaaa...,you WON!!!")
                                
                                gameover=True
                            else:
                                nextnum()
                                display()
                                if lose():
                                    print("sorry, you lost .you dont have more steps to play")
                                    
                                    gameover=True
                                    
        elif v==2 and boardsize==1:
                display()
                print("you WON!!!")

        elif v>2 and boardsize==1:
                display()
                print("sorry you lose")
except Exception as e:
        print(e)
  






 


    









    
     
