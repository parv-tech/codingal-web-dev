# Normal Function . 

def normal_function() : 
    print("apple")
    print("lychee")
    print("mango")
    print("watermelon")
    print("cherry")
    print("banana")
normal_function()

# Function with return statement . 

def addition_function() : 
  num = int(input("Enter your number : "))
  num2 = int(input("Enter another number : "))
  c = num + num2
  return c

sum = addition_function()

print("Sum of the numbers is" ,sum )

# Function with parameter

def subtraction_function(a , b) :
   c = a-b 
   return c
difference = subtraction_function(5 , 10)

print("The difference of the numbers is " , difference)
      
