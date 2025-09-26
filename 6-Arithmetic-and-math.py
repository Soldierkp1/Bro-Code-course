# import math

# friends = 0

# friends = friends + 1
# #or, use an augmented assignment operators.
# friends += 1

# same thing with other(*, -, /, %(modulus: gives you the remainder of the operation), **) operators.

# result = round(x)
# result = abs(y) --> finds absolute value, is the distance from 0 as a whole number, will return a positive always.
# result = pow(y, z) --> raise a base to a given power.
# result = max(x, y, z) --> gives you the maximum value between the arguments.
# result = min(x, y, z) --> gives you the minimum value between the arguments.

# print(result)

# x = 9.1
# y = 4
# z = 5

# print(math.pi) --> prints the value of Pi.
# print(math.e) --> prints the value of the constant E(exponential constant).
# print(math.sqrt(x)) --> prints the square root of the given value, can also be assigned to a variable.
# print(math.ceil(x)) --> will make it round a number up. Can be assigned to a variable.
# print(math.floor(x)) --> will make it round a number down. Can be assigned to a variable


#EXCERCISE 1: CALCULATE DE CIRCUMFERENCE OF A CIRCLE.
#Formula: C = 2*pi*r
#import math. 

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference of your circle is: {round(circumference, 2)}")

#EXCERCISE 2: CALCULATE THE AREA OF A CIRCLE.
#Formula: A = pi*r**2

# radius = float(input("Enter your circle radius: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the cirlce is: {round(area, 2)}")

#EXCERCISE 3: FIND THE HIPOTENUSE OF A RIGHT TRIANGLE.
#Formula = c = sqrt(a**2 + b**2)

# side_a = float(input("Enter the side A: "))
# side_b = float(input("Enter the side B: "))

# c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
# print(f"The side C equals: {c}")

