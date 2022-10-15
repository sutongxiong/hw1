"""
Author: Sutong Xiong
Assignment / Part: HW5 - Q1
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_input = str(input("Say something: "))
input_length = len(user_input)
total_unchanged = 0
total_changed = 0
total_non_alphabetic = 0

for character in user_input:
    if 65 <= ord(character) <= 90:
        print(chr(ord(character)+32), end="")
        total_changed += 1
    elif 97 <= ord(character) <= 122:
        print(character, end="")
        total_unchanged += 1
    else:
        print(character, end="")
        total_non_alphabetic+=1

print()
print("Number of changed letters:", total_changed)
print("Number of unchanged letters:",total_unchanged)
print("Number of non-alphabetic characters:",total_non_alphabetic)
