import random

PossibleValues=["S","P","R"]
CompValue=random.choice(PossibleValues)

UserScore, CompScore, TieGames = 0, 0, 0
count=1
while count<=10:
    print(f"Game Number : {count}")
    print("Enter your choice :")
    print("S - STONE\n","P - PAPER\n","R - SCISSOR")
    val=input()
    UserValue=val.upper()


    print(f"Computer Choose : {CompValue}","\t\t\t",f"You Choose : {UserValue}")
    if UserValue not in ["S","P","R"]:
        print("Invalid Input, Please try again")
        print("S - STONE\n", "P - PAPER\n", "R - SCISSOR")
        val = input()
        UserValue = val.upper()

    if CompValue==UserValue:
        print("It's a Tie")
        TieGames+=1


    elif CompValue=="S":
        if UserValue=="P":
            print("Congratulations you won")
            UserScore+=1
        else:
            print("Computer Won")
            CompScore+=1

        print(f"User Won : {UserScore} games", "\t\t\t", f"Computer Won : {CompScore}","\t\t\t",f"Tie Games : {TieGames}")


    elif CompValue=="P":
        if UserValue=="R":
            print("Congratulations you won")
            UserScore+=1
        else:
            print("Computer Won")
            CompScore+=1

        print(f"User Won : {UserScore} games", "\t\t\t", f"Computer Won : {CompScore}","\t\t\t",f"Tie Games : {TieGames}")


    else:
        if UserValue=="S":
            print("Congratulations you won")
            UserScore+=1
        else:
            print("Computer Won")
            CompScore+=1

        print(f"User Won : {UserScore} games", "\t\t\t", f"Computer Won : {CompScore}","\t\t\t",f"Tie Games : {TieGames}")
    print("****************************************************************************")
    count+=1
print("Game Over")
print(f"Final Score : Computer Won : {CompScore} games\t User Won : {UserScore} games \t Tie Games :{TieGames}")

if UserScore>CompScore:
    print("Congratulation you won the Game")
elif CompScore>UserScore:
    print("Unfortunately you lost the Game")
else:
    print("Hard Luck, It's a Tie")