
import random
numb = random.randint(0, 11)
#print(numb)
guesses_letf = 3


while guesses_letf > 0:
    usrnr = int(input("Please guess number in range 0 - 10: "))
    if usrnr == numb:
        print("You guessed the number and won!")
        break
    #elif a != x:
    #    print("Not correct number, please try again.")
    guesses_letf -= 1
else:
    print("You lose!")