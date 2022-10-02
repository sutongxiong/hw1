"""
Author: Sutong Xiong
Assignment / Part: HW3 - Q5
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

first_side = round(float(input("Length of the first side: ")), 5)
second_side = round(float(input("Length of the second side: ")), 5)
third_side = round(float(input("Length of the first side: ")), 5)
triangle_type = ""

if first_side == second_side == third_side:
    triangle_type = "an equilateral triangle"
elif first_side == second_side or second_side == third_side or first_side ==third_side:
    if first_side**2 == second_side**2*2 or second_side **2 == first_side**2*2 or third_side**2 == first_side**2*2:
        triangle_type = "an isosceles right triangle"
    else:
        triangle_type = "an isosceles triangle that is not a right triangle"
else:
    triangle_type = "a triangle that is not an isosceles and not an equilateral (i.e. scalene)"
first_side = str(first_side)+","
second_side = str(second_side)+","
print(first_side, second_side, third_side, "form", triangle_type)