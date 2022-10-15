"""
Author: Sutong Xiong
Assignment / Part: HW5 - Q3
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_input = str(input("Please enter a string of lowercase letters: "))
previous_character = user_input[0]
is_decreasing = True

for character in user_input[1:]:
    if ord(character)<ord(previous_character):
        previous_character = character
        is_decreasing = True
    else:
        is_decreasing = False

if is_decreasing is True:
    print(user_input, "is decreasing.")
else:
    print(user_input, "is not decreasing.")


