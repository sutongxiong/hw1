"""
Author: Sutong Xiong
Assignment / Part: HW3 - Q4
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import math

value_a = float(input("Enter the value of a: "))
value_b = float(input("Enter the value of b: "))
value_c = float(input("Enter the value of c: "))

number_of_solutions = 1

if value_a == 0:
    if value_b == 0:
        if value_c == 0:
            print("This function has infinite number of solutions.")


elif value_a*value_c*4 > value_b**2:
    print("The funtion has no real solution.")
elif value_a*value_c*4 == value_b**2:
    print("The funtion has one solution. x=", (-value_b + math.sqrt(value_b ** 2 - 4 * value_a * value_c))/2/value_a)
else:
    print("This equation has 2 solutions: x =", (-value_b + math.sqrt(value_b ** 2 - 4 * value_a * value_c)) / 2 / value_a, "x=", -value_b - math.sqrt(value_b ** 2 - 4 * value_a * value_c)/ 2 / value_a)

