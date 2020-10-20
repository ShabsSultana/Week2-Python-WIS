#Extention of guessing game created in week 1
#Additions:
    # 1. Give user 6 guesses
    # 2. Indicate whether the guess is too high or too low
#outline:
    # 1. ask for user's name
    # 2. Welcome to guessing game, number between 2 values, you have 6 guesses
    # 3. while guessNumber > 0, 


import random

#asks user for name
userName = input("Hello, enter your name: ")
#picks a random number between the numbers in the brackets
number = random.randint(1,20)
#number of guesses a user has
guessNumber = 6
#game instructions
print("Well " + userName + ", I am thinking of a number between 1 and 20")
print ("You have " + str(guessNumber) + " guesses to pick the correct number")

while (guessNumber > 0):
    print("Take a guess!")
    guess = int(input())
    guessNumber = guessNumber - 1
    
    #if user's guess is correct, tell user and break the loop
    if (guess == number):
        print("Good job " + userName + ", you guessed my number!")
        break
    
    #if guess is not between 1 and 20, tell user than it's not in the range of numbers
    elif not 1 <= guess <= 20 :
        print("Out of range") or guess < 0

    #if no more guesses left
    elif(guessNumber == 0):
        print("You have run out of guesses, better luck next time!")

    #if the guess is too high, usser is told so 
    elif (guess > number):
        print("You guessed too high")
        #changes grammar based on numbers
        if (guessNumber == 1):
            print("You have " + str(guessNumber) + " guess left")
        else:
            print("You have " + str(guessNumber) + " guesses left")
    
    #if the guess is lower than the actual number then tell user that it's too low
    elif (guess < number):
        print("You guessed too low")
        #changes grammar based on numbers
        if (guessNumber == 1):
            print("You have " + str(guessNumber) + " guess left")
        else:
            print("You have " + str(guessNumber) + " guesses left")
    
   

