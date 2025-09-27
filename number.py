import random

playing = True
number = str(random.randint(1,60))

print("I will generate a number from 1 to 60, and you have to guess that number!!")

while playing:

    guess = input("Give me your best guess! \n")

    if number == guess:
       print("You win the game")
       print("The number was", number)
       break

    else:
        print("Your guess is not quite right, try again. \n")