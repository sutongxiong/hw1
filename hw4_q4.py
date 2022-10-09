"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q4
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_input=int(input("Please enter a positive integer: "))
current_string = ""

for number_a in range(1,user_input+1):
    even_digit = odd_digit = 0
    current_number = number_a

    while current_number != 0:
        if current_number%2 == 0:
            even_digit += 1
        else:
            odd_digit += 1
        current_number = current_number//10

    if even_digit > odd_digit:
        number_a = str(number_a)
        current_string = current_string+number_a+" "

print(current_string)

