import turtle as turtle_module
import random

turtle_module.colormode(255)
myturtle=turtle_module.Turtle()

myturtle.speed("fastest")
myturtle.penup()
myturtle.hideturtle()

myturtle.setheading(225)
myturtle.forward(300)
myturtle.setheading(0)

color_list=[(249, 248, 248), (232, 241, 239), (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218)]
number_of_dots=100

for dot_color in range(1,number_of_dots+1):
    myturtle.dot(20, random.choice(color_list))
    myturtle.forward(50)

    if dot_color%10==0:
        myturtle.setheading(90)
        myturtle.forward(50)
        myturtle.setheading(180)
        myturtle.forward(500)
        myturtle.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()