print("Guess Game\n")

NumtoGuess=20
Guessleft=5
Guesstook=0
while (Guessleft!=0):
    print("Enter your Guess")
    guessed=int(input())

    if(guessed>NumtoGuess):
        print("Guess a smaller number \n")
        Guessleft-=1
        Guesstook+=1
        print("Guesstook : ",Guesstook,"   ","Guessleft : ",Guessleft)
        continue
    elif(guessed<NumtoGuess):
        print("Guess a greater number")
        Guessleft-=1
        Guesstook+=1
        print("Guesstook : ", Guesstook, "   ", "Guessleft : ", Guessleft)
        continue
    else:
        print("You guessed it correctly")
        break
    print("Game Over, you exceeded you guessing limit")
