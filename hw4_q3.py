"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q3
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

row_number = int(input("Enter a positive integer: "))


for rows in range(1,row_number+1):
    num_spaces = row_number - rows
    print(num_spaces * " ", end='')

    for column in range(rows, 0, -1):

        print(str(column), end="")
    print()



