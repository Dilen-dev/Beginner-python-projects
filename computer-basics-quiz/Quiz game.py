#This is a Computer Quiz game, its asks about the acronyms that are basic in computers

# ------This below statement serves to show program has started and also welcomes the user to the quiz
print("Welcome to my computer quiz!")

#------This below statement asks the user is they want to play the game
playing = input("Do you want to play? ")

#------This below statement checks where the user typed in yes, if not then the program quits(is closed)
if playing.lower() != "yes": #------The .lower() function makes everything typed to be in lowercase, this fixed the YES != yes problem
    quit()

print("Okay! Let's play 😊") #------This is only displayed onces the user wants to play
score = 0

answer = input("What does CPU stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "central processing unit" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "graphics processing unit" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("what does RAM stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "random access memory" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "read-only memory" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("what does PSU stand for ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "power supply" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does OS stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "operating system" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "hard disk drive" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "universal serial bus" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does VGA stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "video graphics array" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input("What does PDF stand for? ")
#------This below stament checks whether the answer inserted for the question above is correct and prints correct if it is and incorrect if its not
if answer.lower() == "portable document format" : 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

#------This statements below provide the score the user
print("You got " +str(score) + " questions correct!")
print("You got " +str((score/10)*100) + " %")