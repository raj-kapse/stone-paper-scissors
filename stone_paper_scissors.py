import random
computer = random.choice([0,-1,1])
print("stone,paper,scissor are options choose your option")
youStr = input("Enter Your Choice: ")
youDict = {"paper":0,"stone":-1,"scissor":1}
youStr = youStr.lower()
you = youDict[youStr]
reverseDict={0:"paper",-1:"stone",1:"scissor"}
print(f"your choice:{reverseDict[you]} \ncomputer choice:{reverseDict[computer]}")
if(computer==you):
    print("Its a Draw")
else:
    if(you==-1 and computer==0):
        print("you lose!")
    elif(you==1 and computer==0):
        print("you win!")
    elif(you==0 and computer==1):
        print("you lose!")
    elif(you==0 and computer==-1):
        print("you win!")
    elif(you==-1 and computer==1):
        print("you win!")
    elif(you==1 and computer==-1):
        print("you lose!")
    else:
        print("wrong selection!")
