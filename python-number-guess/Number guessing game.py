import random

top_of_range = input("Type a number: ")

#------The below statement checks if what was passed in by the user is a digit and if it is, the digit is converted from string format to integer format
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
#-----This below statement checks if the number is larger than zero if not it dislays the message and quits the program
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else: #------This applies for when the user has entered something that is not a number such as a word or a symbol
    print("Please type a number next time")
    quit()

random_number = random .randrange(top_of_range)#------This is a form of random number generation where the upper bound is not part of the numbers generated
guesses = 0
#-----This below statement checks if the number is larger than zero if not it dislays the message and quits the program
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
      user_guess = int(user_guess)
    else:
        print("Please type a number larger than 0 next time")
        continue

    if user_guess == random_number:
        print("You got it!🥳🎊")
        break
    elif user_guess > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")



print("You got it in", guesses, "guesses")#-----This is equivalent to print("You got it in " + str(guesses) + " guesses")
