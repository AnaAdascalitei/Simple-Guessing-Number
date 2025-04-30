#number guessing game 
'''
user selects a range
A -> B
random no from the interval will be selected by the compiler
the user has to guess it in the min no of guesses

when the user has less than 3 guess remaining, it gets hints
'''
import random

noA = int(input("Choose where the range starts:"))
noB = int(input("Choose where the range ends:"))

guessNo = random.randrange(noA, noB)
guessCounter = 7
ok = 0

print("You have 7 chances to guess the number")

while guessCounter > 0:
    
    if guessCounter < 3:
        print(f"Be careful, you have only {guessCounter} guesses left", end = '\n')
    
    try:
        noUser = int(input("\nYour guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if(noUser == guessNo):
        print(f"Good job!You guessed the number in {7 - guessCounter + 1} guesses")
        ok = 1
        break
    
    elif noUser < guessNo:
        print("Wrong number! Try again :<")
        guessCounter -=1
        print(f"Here is a hint! The number you have to guess is greater than {noUser}")
    
    else:
            print("Wrong number! Try again :<")
            guessCounter -=1
            print(f"Here is a hint! The number you have to guess is smaller than {noUser}")
                    
                    
if guessCounter == 0 & ok == 0:
    print(f"\nYou didn't guess the number :( The number you had to guess was {guessNo}")
                    

        