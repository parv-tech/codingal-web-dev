# Draw a face using turtle graphics in oops concepts

import turtle

class SmilyFace:

# Constructor to initialize the turtle and screen

    def __init__(self):

        self.t = turtle.Turtle()

        self.t.speed(1)

        self.turtle_screen = turtle.Screen()

        self.turtle_screen.bgcolor("blue")

        self.t.color("red", "green")


# Method to draw a filled circle

    def draw_circle(self, x, y, radius):

        self.t.penup()

        self.t.goto(x, y - radius)

        self.t.pendown()

        self.t.begin_fill()

        self.t.circle(radius)

        self.t.end_fill()

# Method to draw eyes

    def draw_eye(self, x, y):

        self.draw_circle(x, y, 10)

# Method to draw a mouth

    def draw_mouth(self):

        self.t.penup()

        self.t.goto(-50, -20)

        self.t.pendown()

        self.t.setheading(-60)

        self.t.circle(50, 120)

# Method to draw the entire face

    def draw_face(self):

        self.draw_circle(0, 0, 100)

        self.draw_eye(-35, 40)

        self.draw_eye(35, 40)

        self.draw_mouth()


# Method to run the turtle graphics

    def run(self):

        self.draw_face()

        turtle.done()


# Create a FunkyFace object and run it

funky_face = SmilyFace()

funky_face.run()