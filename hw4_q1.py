"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q1
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
number_of_rows = 1
number_printed = 1
count =1
positive_integer = int(input("Please enter a positive integer: "))
print("Executing while-loop...")
while count <= positive_integer:
    print(number_of_rows)
    number_of_rows +=2
    count +=1
count = 1
print()
print("Executing for-loop...")
for rows in range(1,positive_integer+1):
    print(number_printed)
    number_printed +=2
    count +=1

