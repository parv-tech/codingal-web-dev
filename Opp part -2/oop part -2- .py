# Write a code to find the area of a rectangle using oop concepts

class Rectangle:

 def __init__(self, length, width):

  self.length = length

  self.width = width

 def area(self):

  return self.length * self.width


areaofRec = Rectangle(12, 10)

print(areaofRec.area())