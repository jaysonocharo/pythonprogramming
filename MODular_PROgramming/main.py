# FIRST METHOD OF IMPORTING:
    #(BEST for importing)

#import functions
#x = functions.add(12,34)
#y = functions.subtract(45,23)
#print(y)

# SECOND METHOD OF IMPORTING:;;

#from operators import add
#from operators import subtract
#x = add(23,45)
#y = subtract(90,25)
#print(x)
#print(y)

import operators
import others
import trig

#x = others.cube(9)
#y = operators.add(7,8)

#print(x)
#print(y)
operator = input("Enter operator:")

if operator == "cube":
    num = eval(input("Enter number: "))
    x = others.cube(num)
    print(x)

elif operator == "sin":
    angle = eval(input("Enter angle in degrees: "))
    sin_of_angle = trig.get_sine(angle)
    print(sin_of_angle)

elif operator == "tan":
    angle = eval(input("Enter angle in degrees: "))
    print(trig.get_tan(angle))

elif operator == "cos":
    angle = eval(input("Enter angle in degrees: "))
    print(trig.get_cos(angle))

else:
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))

    if operator == "+":
        x = operators.add(num1,num2)
        print(x)

    elif operator == "-":
        x = operators.subtract(num1,num2)
        print(x)

    elif operator == "/":
        x = operators.divide(num1,num2)
        print(x)

    elif operator == "*" or "x" or "X":
        x = operator.multiply(num1,num2)
        print(x)


