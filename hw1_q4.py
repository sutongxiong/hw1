"""
Author: Sutong Xiong
Assignment / Part: HW1 - Q4
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount of dollars and cents, in two separate lines.")
dollar_value = int(input(""))
cent_value = int(input(""))

total_cent = dollar_value*100 + cent_value
quarter_num = total_cent//25
dime_num = (total_cent-quarter_num*25)//10
nickel_num = (total_cent-quarter_num*25-dime_num*10)//5
penny_num = (total_cent-quarter_num*25-dime_num*10)%5

print(dollar_value,"dollars and", cent_value,"cents are:", quarter_num,'quarters,', dime_num, 'dimes,', nickel_num, 'nickels, and', penny_num,'pennies.')


