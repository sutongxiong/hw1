"""
Author: Sutong Xiong
Assignment / Part: HW1 - Q5
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

dean_permission = str(input("Do you have permission from the dean? [y/n] "))
advisor_permission = str(input("Do you have permission from the advisor? [y/n] "))
senior_status = str(input("Do you hold senior status? [y/n] "))
num_credits = int(input("How many credits do you have? "))

can_graduate = (num_credits >= 64 and senior_status == 'y') or (num_credits>=40 and advisor_permission == 'y') or (dean_permission=='y')

print("This student can graduate:", can_graduate)







