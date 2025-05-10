# Day 1

# print("Hello world")

# print("hi this is hemanth")

# print("hi")

# print("Hello")

# Questions to practice (Day-1): 

# 1.Print your name.
#print(" My name is Hemanth")    #My name is Hemanth

# 2.Print the result of adding two numbers.
#print(42+63)                    #105

# 3.Print the result of subtracting two numbers.
#print(144-1)                    #143

# 4.Print the result of multiplying two numbers.
#print(7*9)                      #63

# 5.Print the result of dividing two numbers.
#print(144/12)                    #12.0

# Day 2

#variables
# a = "nihar"
# b = " is a "
# c = "good boy"
# print(a+b+c)

# a = input("Enter your Name ")
# print("Your name is: " +a) 

#datatypes

# a = 1                 #int datatype for integers
#b = "hemanth"          #str datatype for characters
#c = 3.33                #float datatype is for decimals 
#d = True                #bool datatype is for boolean expressions like true or false 
# print(type(a))
# print(type(b))
# print(type(c)) 
# print(type(d))

# Questions to Practice (Day - 2):

# 1.Declare two variables `a` and `b`, assign integer values to them, and print their sum.
#    Expected Output: The sum of `a` and `b`.

# a = 42
# b = 63
# print(a+b )                                 #105

# 2.Create a variable `name` and assign your name to it. Print a greeting message using your name.
#   Expected Output: Greeting message with your name, e.g., "Hello, John!"

# name = "Hemanth"
# print("Hello " +str( name ))                #Hello Hemanth

# 3.Define a variable `pi` and assign the value of π (pi) to it. Print the value of `pi`.
#    Expected Output:The value of π (pi), e.g., 3.14159.

# pi = 3.14159
# print(pi)                                   #3.14159

# 4. Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type.
#    Expected Input: "True" or "False"
#    Expected Output: The data type of the converted boolean.

# user_input = input("Is it raining ? Enter 'True' or 'False' " )
# is_raining = user_input == "True"
# print(type(is_raining))                     #<class bool>

# 5. Create a string variable sentence containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times.
#    Expected Input: A number (e.g., "3")
#    Expected Output:The sentence repeated the specified number of times.

# a = "Hey I am eager to learn Python!"

# b= int(input("Enter the number:"))

# for _ in range(b):
#     print(a)

#6. Given two variables `x` and `y`, perform the following operations and print the results:
    # - Addition of `x` and `y`.
    # - Subtraction of `y` from `x`.
    # - Multiplication of `x` and `y`.
    # - Division of `x` by `y`.
    # - `x` raised to the power of `y`.
    # - The remainder when `x` is divided by `y`.
    # - The floor division of `x` by `y`.

# x = int(input("Enter the value of x:"))                             #8
# y = int(input("Enter the value of y:"))                             #22

# print("Addition of x and y :" +str(x+y))                            #30
# print("Subtraction of x and y:"+str(x-y))                           #-14
# print("Multiplication of x and y:" +str(x*y))                       #176
# print("Division of x and y:"+str(x/y))                              #0.36363636363636365
# print("x raised to the power of y:"+str(x**y))                      #73786976294838206464
# print("The remainder when x is divided by y:"+str(x % y))           #8
# print("The floor division of x and y:"+str(x // y))                 #0

# 7. Define a variable `value` and assign any numerical value to it. Ask the user to input a new value. Update the variable `value` with the new input and print the updated value.
# - Expected Input: A numerical value (e.g., "42")
# - Expected Output: The updated value of the variable.

# value = 63
# i = int (input("enter the new number: "))
# value = float(i)
# print("Updated value: ", value)                                      #42.0

