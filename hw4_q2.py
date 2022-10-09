"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q2
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_input = int(input("Enter a positive integer: "))
for row in range(1,user_input+1):
    print(" "*(row-1) + "*"*(2*user_input-2*row+1)+" "*(row-1))
for row in range(user_input-1):
    print(" "*(user_input-row-2) + "*"*(row*2+2*user_input-5) + " " * (user_input-row-2))



