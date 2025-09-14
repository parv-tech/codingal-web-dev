# draw square using turtle with oops concept

import turtle

class Square:

# Constructor to initialize the turtle and side length

    def __init__(self, side_length):

        self.side_length = side_length

        self.t = turtle.Turtle()

# Instance Method to draw the square

    def draw(self):

        for _ in range(4):

            self.t.forward(self.side_length)

            self.t.right(90)



# Create a square object with side length 100

square = Square(100)

# Draw the square

square.draw()

turtle.exitonclick() # Keep the window open until clicked