# import colorgram
#
# colors = colorgram.extract('image.jpg', 100)
# colors_list = []
# rgb_list = []
# for color in colors:
#     colors_list.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     rgb_list.append(color_tuple)
#
# print(colors_list)
# print(rgb_list)
# print(len(colors_list))
# print(colors_list[0])
# print(colors_list[0][0])
from turtle import Turtle, colormode, Screen
import random

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
colormode(255)
tim = Turtle()


def one_line():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

tim.hideturtle()
tim.speed('fastest')
tim.penup()
tim.goto(-250, -250)
for i in range(1, 11):
    print(i)
    one_line()
    # tim.home()
    tim.goto(-250, -250 + (50 * i))

print(tim.xcor())
print(tim.ycor())


screen = Screen()
screen.exitonclick()
