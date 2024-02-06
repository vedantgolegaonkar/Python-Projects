# The Below code is used to extract the colors from the images, which is then scored in the variable called color_list

# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('hirst_painting.png',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Main Code
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173),
              (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21),
              (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132),
              (190, 187, 218), (230, 176, 172), (231, 65, 82)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.goto(-225, -225)
tim.pendown()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = turtle_module.Screen()
screen.exitonclick()
