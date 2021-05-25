board={'top-L':' ','top-M':' ','top-R':' ',
      'middle-L':' ','middle-M':' ','middle-R':' ',
       'bottom-L':' ','bottom-M':' ','bottom-R':' '}
def showboard():
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['middle-L']+'|'+board['middle-M']+'|'+board['middle-R'])
    print('-+-+-')
    print(board['bottom-L']+'|'+board['bottom-M']+'|'+board['bottom-R'])

def makemove(x,y,move):
        place=" "
        if y==1 and x==1:
            place='bottom-L'
        elif y==1 and x==2:
            place='bottom-M'
        elif y==1 and x==3:
            place='bottom-R'
        elif y==2 and x==1:
            place='middle-L'
        elif y==2 and x==2:
            place='middle-M'
        elif y==2 and x==3:
            place='middle-R'
        elif x==1 and y==3:
            place='top-L'
        elif x==2 and y==3:
            place='top-M'
        elif x==3 and y==3:
            place ='top-R'
        board[place]=move
            
            
        




ans = input("Let's play a game of tic tac toe (y/n): ")
if ans=='y':
    while ans=='y':
        showboard()
        print("\n")
        move=input("Player one choose X or O: ")
        for i in range(0,9):
            if i%2==0:
                print("It's player one's move")
                x=input("Enter column: ")
                y=input("Enter row: ")
                makemove()
        