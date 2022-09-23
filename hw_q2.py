"""
Author: Sutong Xiong
Assignment / Part: HW1 - Q2
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

year_input = int(input("Please enter a year greater than 2022: "))
year_passed = year_input - 2022

total_second = year_passed*365*24*3600
new_birth = total_second//9
new_death = total_second//18
new_immigrant = total_second//40
new_emigrant = total_second//60
future_population = new_immigrant-new_emigrant+new_birth-new_death + 330109174

print("The population in year", year_input, "will be", future_population)

