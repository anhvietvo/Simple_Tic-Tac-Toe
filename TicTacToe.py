import random

row = [""] * 9
availablenum = [1,2,3,4,5,6,7,8,9]

#Create a function to print tic-tac-toe table
def theboard():
    divideline = "{:-<5}-{:-^5}-{:->5}" .format("", "", "")
    print("{:^17}" .format("AVAILABLE MOVES") + "\t" + "{:^17}" .format("TIC-TAC-TOE"))
    print("{:^5}|{:^5}|{:^5}" .format(row[0],row[1],row[2]) + "\t" + "{:^5}|{:^5}|{:^5}" .format(availablenum[0],availablenum[1],availablenum[2]))
    print(divideline + "\t" + divideline)
    print("{:^5}|{:^5}|{:^5}" .format(row[3],row[4],row[5]) + "\t" + "{:^5}|{:^5}|{:^5}" .format(availablenum[3],availablenum[4],availablenum[5]))
    print(divideline + "\t" + divideline)
    print("{:^5}|{:^5}|{:^5}" .format(row[6],row[7],row[8]) + "\t" + "{:^5}|{:^5}|{:^5}" .format(availablenum[6],availablenum[7],availablenum[8]))
    print("\n")

#Create a function to check the possition is free
def free(num):
    if (num < 1 or num > 9):
        return False
    return row[num-1] == ""
        
        
#Create a function to check the winner
def check():
    return (row[1] == row[4] == row[7] != "" or 
           row[2] == row[5] == row[8] != "" or 
           row[0] == row[3] == row[6] != "" or 
           row[0] == row[1] == row[2] != "" or 
           row[3] == row[4] == row[5] != "" or 
           row[6] == row[7] == row[8] != "" or 
           row[0] == row[4] == row[8] != "" or 
           row[2] == row[4] == row[6] != "")

#Create a function to check the board full
def full():
    fullnum = 0
    for i in range(9):
        if str(row[i]) .isalpha() == True: 
           fullnum += 1
    return fullnum == 9

#Create a function to place XO to the table and then print the table
def place(num, signal):
    row[num - 1] = signal
    availablenum[num-1] = ""
    theboard()
    
if __name__ == "__main__":
    #input players' name
    player1 = input("What is the first player's name: ")
    player2 = input("What is the second player's name: ")
    #random a player go first
    first = random.choice([player1, player2]) 
    if first == player1:
        second = player2
    else:
        second = player1
    #Let's start the TIC-TAC-Toe
    while True:
        enter = input("TYPE 'ENTER' TO PLAY THE GAME: ") .lower()
        if enter == "enter":
            print("{} will go first." .format(first))
            n = input("{}: Do you want to be X or O? Enter here: " .format(first)) .upper()
            while n != "X" and n != "O":
                n = input("Only X or O. Please enter again: ") .upper()
            if n == "X":
                n1 = "O"        
            else:
                n1 = "X"
        else:
            break
        #Ready or not?    
        ready = input("Are you ready to play? Enter Yes or No: ") .lower()
        while (ready != "yes" and ready != "no"):
            ready = input("Please enter only YES or NO: ") .lower()
        if ready == "no":
            break
        #The game begin    
        while True:
            theboard()
            #X turn
            firstturn = int(input("{} is {}'s signal. Enter a number (1-9). Your number is: " .format(n, first)))

            #Check the possition
            while (not free(firstturn)):
                firstturn = int(input("Wrong position. Please choose again: "))

            #Place X to the table and then print the table
            place(firstturn, n)
                
            #Check X in case X is the winner
            if check():
                print("CONGRATULATIONS {}! You won!" .format(first))
                break
        
            #Check the board is full or not and playagain
            if full():
                print("The board was full. The game is draw!")
                break
            
            #O Turn
            secondturn = int(input("{}'s signal is {}. Your position (1-9) is: " .format(second,n1)))
        
            #Check the possition
            while free(secondturn) == False:
                secondturn = int(input("Wrong position! Please choose again: "))
                
            #Place O to the table and then print the table
            place(secondturn, n1)
        
            #Check O in case O is the winner
            if check() == True:
                print("Congratulations {}. You won!" .format(second))    
                break      
        

        play_again = input("GAME OVER! DO YOU WANT TO PLAY AGAIN? YES OR NO: ") .upper()
        while play_again != "YES" and play_again != "NO":
            play_again = input("WHAT DO YOU MEAN? ONLY YES OR NO?: ") .upper()    
        if play_again == "YES":
            row = [""] * 9
            availablenum = [1,2,3,4,5,6,7,8,9]
            theboard()
            continue
        else:
            print("THANKS FOR PLAYING!")
            break