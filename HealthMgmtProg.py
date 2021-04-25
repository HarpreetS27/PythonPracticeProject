print("Welcome to Health Management System\n")


clientlist={1:"Matt",2:"Henry",3:"Scott"}
print("Enter the patient number : \n","1.Matt\n","2-Henry\n","3-Scott")

patient=int(input())
while patient not in clientlist.keys():
    print("Please enter the number in range")
    print("Enter the patient number : \n", "1.Matt\n", "2-Henry\n", "3-Scott")
    patient = int(input())
    continue


print("Enter 1 for logging information")
print("Enter 2 to retrieve information\n")
req=int(input())

if req not in [1,2]:
    print("Please enter the number in range")


def writefood():
    print("Enter the food details :")
    food =input()
    return food

def writeexc():
    print("Enter the excercise details : ")
    exc = input()
    return exc



if req==1:
    def getdate():
        import datetime
        return datetime.datetime.now()


    print("Enter 1 to log food entries\n")
    print("Enter 2 to log excercise entry")
    log=int(input())

    if log==1:
        loggedFood=writefood()
        f=open(clientlist[patient]+"-food.txt","a")
        f.write("\n")
        f.write(loggedFood+" "+str(getdate()))
        f.close()


    elif log==2:
        loggedexc=writeexc()
        f=open(clientlist[patient]+"-excercie.txt","a")
        f.write("\n")
        f.write(loggedexc+" "+str(getdate())+"\n")
        f.close


elif req==2:
    print("Enter 1 to view food entries\n")
    print("Enter 2 to view excercise entries")
    view=int(input())
    if view==1:
        try:
            f = open(clientlist[patient]+"-food.txt")
            print(f.read())
            f.close()

        except:
            print("No file available,Please create one")

    elif view==2:
        try:
            f=open(clientlist[patient]+"-excercie.txt")
            print(f.read())
            f.close()
        except:
            print("No file exist,Please create one")
    else:
        print("Invalid input")


