from turtle import Turtle as TurtleAlias, Screen

# # modules, packages, aliases
# import turtle
# tim = turtle.Turtle()
# tim.shape('turtle')
# tim.color('red')

# from turtle import Turtle
# tim2 = Turtle() # more convenient

# from random import * 
# print(choice([1, 2, 3])) # instead of random.choice()

# import turtle as t
# newTurtle = t.Turtle()






# turtle exercises

tim = TurtleAlias()
####### program to print a dashed line

# for _ in range(10):
#     tim.forward(10)
#     tim.penup() # lift the pen (don't draw)
#     tim.forward(10)
#     tim.pendown()

# # another solution
# for _ in range(10):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")


####### program to draw some mathematical shapes
# turtleColors = ['light cyan', 'dark orange', 'indian red', 'dark slate blue']
# import random
# def drawShape(numOfSides):
#     tim.color(random.choice(turtleColors))
#     for _ in range(numOfSides):
#         tim.forward(100)
#         tim.right(360/numOfSides)

# for side in range(3, 11): # 11 is excluded
#     drawShape(side)






# # tuple is like an array but immutable
# myTuple = (1, 3, 8)
# print(myTuple[0], myTuple[1], myTuple[2])
# print(list(myTuple)) # onvert the tuple to array if you want to modify it 



####### program for random walk
# import random
# import turtle
# # turtleColors = ['royal blue', 'midnight blue', 'lawn green', 'maroon', 'magenta', 'indigo']
# def generateRandomColor():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     return (r, b, g) # tuple

# directions = [0, 90, 180, 270]

# turtle.colormode(255)
# tim.pensize(15)
# tim.speed('fastest')
# for _ in range(200):
#     # tim.color(random.choice(turtleColors))
#     tim.color(generateRandomColor())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


####### program to draw spirograph
# import random
# import turtle
# def generateRandomColor():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     return (r, b, g) # tuple

# tim.speed('fastest')
# turtle.colormode(255)

# def drawSpirograph(gap):
#     for _ in range(int(360 / gap)):
#         tim.color(generateRandomColor())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)

# drawSpirograph(5)





# cologram: extract colors from an image
import colorgram
import turtle
import random

newTurtle = turtle.Turtle()
turtle.colormode(255)
newTurtle.speed('fastest')
newTurtle.penup() 
newTurtle.hideturtle() # you will find another arrow (turtle), most likely it is an old decleration in the code

rgbColors = []
colors = colorgram.extract('download.jpg', 6) # Extract 6 colors from an image.

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor = (r, g, b)
    rgbColors.append(newColor) # [(249, 248, 243), (250, 245, 248), (243, 250, 246), (241, 246, 250), (234, 225, 83), (195, 8, 69)]

print(rgbColors) 

newTurtle.setheading(225)
newTurtle.forward(300)
newTurtle.setheading(0)
numberOfDots = 100

for dotCount in range(1, numberOfDots + 1):
    newTurtle.dot(20, random.choice(rgbColors))
    newTurtle.forward(50)

    if dotCount % 10 == 0:
        newTurtle.setheading(90)
        newTurtle.forward(50)
        newTurtle.setheading(180)
        newTurtle.forward(500)
        newTurtle.setheading(0)




myScreen = Screen()
myScreen.exitonclick()