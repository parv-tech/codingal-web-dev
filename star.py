import turtle


my_drawing_is = turtle.Screen()


my_drawing_is.bgcolor("crimson")


my_drawing_is.setup(500 , 400)


turtle.title("my-drawing-is-best")


drawing = turtle.Turtle()

for i in range(5):
    drawing.forward(100)
    drawing.right(144)


my_drawing_is.exitonclick()
