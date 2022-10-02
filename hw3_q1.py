"""
Author: [Your name here]
Assignment / Part: HW3 - Q1 (depending on the file name)
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

current_xp = float(input("Enter this user's current XP: "))
valid_level = False

if 0<=current_xp<18.0:
    valid_level = True
    current_level = 1
elif 18.0<= current_xp<=24.9:
    valid_level = True
    current_level = 2
elif 25.0<=current_xp<=29.9:
    valid_level = True
    current_level = 3
elif 30.0<=current_xp<=39.9:
    valid_level = True
    current_level = 4
elif 40.0<= current_xp <= 50.0:
    valid_level = True
    current_level = 5
else:
    print("ERROR: Please enter a valid XP value.")

current_xp = str(current_xp)+")"

if valid_level == True:
    print("Level", current_level, "Player (XP:", current_xp)