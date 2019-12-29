import random
import sys


def instructions(lists, turns, totalScore):
    
    print("WELCOME TO TIC-TAC-TOE\n")
    print("This will be a two-player game.\n")
    print("Before we began. Let's determine who will go first!\n")
    print("To detemine who goes first:\n We will ask both players to pick a number between 1-10 \n"
          " We will then generate a random number between 1-10\n"
          " Whichever player's number is closer to the random number, will go first \n") 
    toss(lists, turns, totalScore)


def toss(lists, turns, totalScore):
    
    finalResult = []
    player1 = int(input("Player 1, pick a number between 1-10: "))
    player2 = int(input("Player 2, pick a number between 1-10: "))

    while ((player1) < 1) or ((player1) > 10):
        player1 = int(input("Player 1, please pick a number between 1-10: "))

    while ((player2) < 1) or ((player2) > 10):
        player2 = int(input("Player 2, please pick a number between 1-10: "))

    while player1 == player2 :
        print("You both picked the same number, let's try again! \n")
        player1 = int(input("Player 1, pick a number between 1-10: "))
        player2 = int(input("Player 2, pick a number between 1-10: "))
        
    randomNumber = random.randint(1,10)
    
    if (player1 >= randomNumber):
        result = player1 - randomNumber
        finalResult.append(result)

    if (player1 < randomNumber):
        result = randomNumber - player1
        finalResult.append(result)


    if (player2 >= randomNumber):
        result = player2 - randomNumber
        finalResult.append(result)

    if (player2 < randomNumber):
        result = randomNumber - player2
        finalResult.append(result)

    tossWinner(finalResult, randomNumber, lists, turns, totalScore)



def tossWinner(result,randomNumber, lists, turns, totalScore):

    if result[0] < result[-1]:
        print("Generated Random number was:", randomNumber)
        print("Player 1 will go first\n")
        Board(lists)
        player1Turn(lists, turns, totalScore)
        
    if result[0] > result[-1]:
        print("Generated Random number was:", randomNumber)
        print("Player 2 will go first\n")
        Board(lists)
        player2Turn(lists, turns, totalScore)

    if result[0] == result[-1]:
        print("Generated Random number was:", randomNumber)
        print("You both are at the same distance from the random number, let's try again!\n")
        toss(lists, turns, totalScore)

    

def Board(list):

    print("\n")

    ver = '|'
    hor = '----------'
    first = 0
    second = 3
    third = 6
    for y in range(0,3):
        print(list[first],ver,list[second], ver, list[third])
        if y < 2:
            print(hor)

        first = first + 1
        second = second + 1
        third  = third + 1

    print("\n")


        
def player1Turn(lists,turns,totalScore):

    countX = 0
    inputX = input("Player 1 please select a box by entering a number which represents a box: ")
    x = int(inputX)
    
     
    while(countX < len(turns)):
        while(turns[countX] == x):
            inputX = input("Player 1 please reselect a box by entering a number which represents a box: ")
            x = int(inputX)
        countX = countX + 1
        
    turns.append(x)
    if (len(turns) <= 9):
        if((x > -1)and(x < 9)):
            lists[x] = "X"
        Board(lists)

 
    if(len(turns) == 9):
        printList(lists, turns)
        sys.exit()
        
    if((lists[0] == 'X') & (lists[1] == 'X') & (lists[2] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists,turns,totalScore)   
    if((lists[3] == 'X') & (lists[4] == 'X') & (lists[5] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns, totalScore)
    if((lists[6] == 'X') & (lists[7] == 'X') & (lists[8] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[0] == 'X') & (lists[3] == 'X') & (lists[6] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[1] == 'X') & (lists[4] == 'X') & (lists[7] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[2] == 'X') & (lists[5] == 'X') & (lists[8] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[0] == 'X') & (lists[4] == 'X') & (lists[8] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[2] == 'X') & (lists[4] == 'X') & (lists[6] == 'X')):
        print("Player 1 won!")
        printList(lists, turns)
        totalScore['Player1']['Score'] = totalScore['Player1']['Score'] + 1
        playAgain(lists, turns,totalScore)

    player2Turn(lists,turns,totalScore)
    



def player2Turn(lists,turns,totalScore):
    

    countO = 0   
    inputO = input("Player 2 please select a box by entering a number which represents a box: ")
    o = int(inputO)
    

    while(countO < len(turns)):
        while(turns[countO] == o):
            inputO = input("Player 2 please reselect a box by entering a number which represents a box: ")
            o = int(inputO)
        countO = countO + 1

    turns.append(o)
    if (len(turns) <= 9):
        if((o > -1)&(o < 9)):
            lists[o] = "O"
        Board(lists)
  
    if(len(turns) == 9):
        printList(lists, turns)
        sys.exit()
        
    if((lists[0] == 'O') & (lists[1] == 'O') & (lists[2] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[3] == 'O') & (lists[4] == 'O') & (lists[5] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[6] == 'O') & (lists[7] == 'O') & (lists[8] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[0] == 'O') & (lists[3] == 'O') & (lists[6] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[1] == 'O') & (lists[4] == 'O') & (lists[7] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[2] == 'O') & (lists[5] == 'O') & (lists[8] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[0] == 'O') & (lists[4] == 'O') & (lists[8] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)
    if((lists[2] == 'O') & (lists[4] == 'O') & (lists[6] == 'O')):
        print("Player 2 won!")
        printList(lists, turns)
        totalScore['Player2']['Score'] = totalScore['Player2']['Score'] + 1
        playAgain(lists, turns,totalScore)

    player1Turn(lists,turns,totalScore)



def playAgain(lists, turns,totalScore):
    

    again = str(input("\nDo you guys want to play again? (Yes or No): "))

    while (again != 'Yes') and (again != 'No'):
        again = input("Please just enter -> (Yes or No): ")

    if again == 'Yes':
        print("\nScore: ")
        print("Player 1: ", totalScore['Player1']['Score'])
        print("Player 2: ", totalScore['Player2']['Score'])
        print("OK! Once again we will clarify the rules \n")
        
        lists = ['0','1','2','3','4','5','6','7','8']
        turns = []
        instructions(lists, turns, totalScore)
        
    if again == 'No':
        print("\nScore: ")
        print("Player 1: ", totalScore['Player1']['Score'])
        print("Player 2: ", totalScore['Player2']['Score'])
        print("\nThank you for playing our game!")
        sys.exit()

        

        
def printList(lists, turns):
    print(lists)
    print(turns)
    Board(lists)



print("")    
lists = ['0','1','2','3','4','5','6','7','8']
turns = []
totalScore = {'Player1' : {'Score' : 0}, 'Player2' : {'Score' : 0}}
instructions(lists, turns, totalScore)
print("")







