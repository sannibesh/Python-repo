import turtle

turtle.shape("turtle")
turtle.speed(1)

for n in range(21):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

turtle.exitonclick