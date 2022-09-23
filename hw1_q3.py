"""
Author: Sutong Xiong
Assignment / Part: HW1 - Q3
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter number of coins: ")
quarter_num = int(input("Number of quarters: "))
dime_num = int(input("Number of dimes: "))
nickel_num = int(input("Number of nickels: "))
penny_num = int(input("Number of pennies： "))

total_cents = quarter_num*25 +dime_num*10 + nickel_num*5 + penny_num
dollar_value = total_cents//100
cent_remain = total_cents%100
print("The total is",dollar_value, "dollar(s) and",cent_remain,"cent(s)")

