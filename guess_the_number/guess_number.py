import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if(a>n):
        print("lower pls")
    else:
        print("higher number pls")
print(f"you have guessed the number {n} in {guesses} attempts!!!")
print("Congrats")