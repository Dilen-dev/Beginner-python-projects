import turtle
import time
import random

WIDTH,HEIGHT = 500, 500 #------All capitals to denote they are constant values
COLORS = ["red","green","yellow","blue","brown","purple","black","orange","cyan","pink"]


def number_of_racers():
    racers = 0 
    while True:
        racers = input("Insert number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2 - 10. Try again!!!")
        else:
            print("Number is not numeric...  Try again!!!")
            continue


def race(colors):
    turtles = turtle_create(colors)

    while True:
        for racer in turtles:
            move = random.randrange(1, 20)
            racer.forward(move)
            
            x, y = racer.pos() #------This gets the position of the turtles so after moving them so as to determine if they have crossed the finish  line yet 
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def turtle_create(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()#------This is to ensure that as they do not already draw trails
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)#------This is to set them to be to well spaced 
        racer.pendown()
        turtles.append(racer)
    return turtles


def turtle_init():#------This starts up the turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle race🐢!")
    

racers = number_of_racers()
turtle_init()
random.shuffle(COLORS)
colors = COLORS[:racers]#------This takes the number of colors equal to the number of racers we have by slicing
winner = race(colors)
print("The winner is the turtle with the color:",winner)
time.sleep(5)