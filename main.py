import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.penup()
tim.hideturtle()


c_l = [(248, 247, 244), (243, 250, 247), (250, 244, 248), (241, 244, 248), (5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119), (235, 211, 82), (188, 137, 161), (216, 83, 67), (80, 6, 20), (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29), (220, 176, 210), (74, 107, 141), (152, 136, 65), (20, 207, 180), (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158), (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6), (236, 172, 164), (133, 223, 208)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(c_l))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

