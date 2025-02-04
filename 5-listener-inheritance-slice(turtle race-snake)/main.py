#19-turtle race: higher order function-listener
#20-snake game



# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def moveForward():
#     tim.forward(10)
# def moveBackword():
#     tim.backward(10)
# def moveRight():
#     # tim.right(10)
#     tim.setheading(tim.heading() - 10)
# def moveLeft():
#     # tim.left(10) # both works
#     tim.setheading(tim.heading() + 10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# # screen.onkey(key='space', fun=moveForward)
# screen.onkey(moveForward, 'w')
# screen.onkey(moveBackword, 's')
# screen.onkey(moveRight, 'd')
# screen.onkey(moveLeft, 'a')
# screen.onkey(clear, 'c')
# screen.exitonclick()






# ###### 19-turtle race: higher order function-listener

# from turtle import Turtle, Screen
# import random

# screen = Screen()
# screen.setup(width=500, height=400)
# userGuess = screen.textinput('Make your guess', 'Which turtle will win? what color? ')
# colors = ['red', 'green',  'orange', 'purple', 'blue', 'yellow']
# allTurtals = []
# poistionY = -100
# isRaceOn = False


# tim = Turtle()

# for turtleIndex in range(0, 6):
#     newTurtle = Turtle('turtle')
#     newTurtle.penup()
#     newTurtle.color(colors[turtleIndex])
#     newTurtle.goto(x=-230, y=poistionY)
#     poistionY += 40
#     allTurtals.append(newTurtle)

# if userGuess:
#     isRaceOn = True

# while isRaceOn:

#     for turtle in allTurtals:
#         if turtle.xcor() > 230:
#             isRaceOn = False
#             winningColor = turtle.pencolor()
#             if winningColor == userGuess:
#                 print(f'Right answer')
#             else:
#                 print(f'Wrong answer, the winning is the {winningColor} one')

#         randNumber = random.randint(0, 10)
#         turtle.forward(randNumber)

# screen.exitonclick()






#20-snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game!')
screen.tracer(0)

isGameOn = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while isGameOn:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    # Collision with wall
    if snake.collidedWithWall():
        isGameOn = False
        scoreboard.gameOver()

    # Collision with tail
    for segment in snake.segments:
        if segment == snake.head: 
            pass
        elif snake.head.distance(segment) < 10:
            isGameOn = False
            scoreboard.gameOver()
    


screen.exitonclick()


# slice


numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(numbers[2:5]) # 2 excluding ['c', 'd', 'e']
print(numbers[2:]) # from index 2 to the end ['c', 'd', 'e', 'f', 'g']
print(numbers[:2]) # everything from 0 to 5 excluding  ['a', 'b', 'c', 'd', 'e']
print(numbers[2:5:2]) # start, end, step >>> ['c', 'e']
print(numbers[::2]) # ['a', 'c', 'e', 'g']
print(numbers[::-1]) # reverse the array