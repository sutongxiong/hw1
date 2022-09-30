"""
Author: Sutong Xiong
Assignment / Part: HW3 - Q2
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import random

current_level = float(input("What's this Pokemon's level? "))
pokemon_speed = float(input("What's this Pokemon's speed? "))
critical_hit = False

R = random.randint(0,255)
T = (pokemon_speed/2)
if R<T:
    critical_hit = True
    damage_multiplier = (2*current_level+6)/(current_level+6)
    damage_multiplier = str(round(damage_multiplier, 2)) + "x"
else:
    print("No critical hit. The pokemon's damage would be the same.")


print("The Pokemon's move will be", damage_multiplier, "stronger!")



