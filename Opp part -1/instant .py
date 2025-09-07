class Dog:
    
 def __init__(self, name, breed):

  self.name = name # Instance attribute

  self.breed = breed # Instance attribute

def bark(self): # Instance method

  print(f"{self.name} says Woof!")

  def describe(self): # Another instance method

   print(f"{self.name} is a {self.breed}.")

# Create instances of the Dog class

my_dog = Dog("Buddy", "Golden Retriever")

another_dog = Dog("Max", "Labrador")

# Call instance methods on the objects

my_dog.bark()

my_dog.describe()
 
another_dog.bark()

another_dog.describe()