"""
Author: Sutong Xiong
Assignment / Part: HW5 - Q2
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

first_sequence = str(input("Enter a DNA sequence: "))
second_sequence = str(input("Enter a DNA sequence: "))
a_character_added =0
b_character_added =0
final_sequence = ""
valid_character = True
total_invalid = 0

new_sequence =""
if len(first_sequence)==len(second_sequence) or len(first_sequence)<len(second_sequence):
    for character in range(2*len(first_sequence)):
        if character%2==0:
            new_sequence+=first_sequence[a_character_added]
            a_character_added+=1
        elif character%2==1:
            new_sequence += second_sequence[b_character_added]
            b_character_added +=1

if len(first_sequence)<len(second_sequence):
    new_sequence += second_sequence[b_character_added:]


if len(first_sequence)> len(second_sequence):
    for character in range(2*len(second_sequence)):
        if character%2==0:
            new_sequence+=first_sequence[a_character_added]
            a_character_added+=1
        elif character%2==1:
            new_sequence += second_sequence[b_character_added]
            b_character_added +=1
    new_sequence += first_sequence[a_character_added:]

for character in new_sequence:
    if ord(character) == 65:
        character = chr(ord(character) + 19)
        valid_character = True

    elif ord(character) == 67:
        character = chr(ord(character) + 4)
        valid_character = True

    elif ord(character) == 84:
        character = chr(ord(character) - 19)
        valid_character = True

    elif ord(character) == 71:
        character = chr(ord(character) - 4)
        valid_character = True
    else:
        valid_character = False
        total_invalid += 1

    if valid_character is True:
        final_sequence += character

print("Fused sequence:",final_sequence,"| Invalid characters:", total_invalid)


