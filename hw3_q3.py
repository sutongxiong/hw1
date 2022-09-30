"""
Author: Sutong Xiong
Assignment / Part: HW3 - Q3
Date due: 2022-10-06, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

day_entered = input("Enter the day the call started at: ")
time_entered = int(input("Enter the time the call started at (hhmm): "))
duration_entered = int(input("Enter the duration of the call (in minutes): "))

if day_entered =="Sun" or day_entered =="Sat" or day_entered == "Fri":
    rate_charged = 0.10
if day_entered =="Mon" or day_entered =="Tue" or day_entered =="Wed" or day_entered =="Thr":
    if 500<time_entered or time_entered>2100:
        rate_charged = 0.35
    else:
        rate_charged = 0.55

total_cost = "$" + str(round(rate_charged * duration_entered,1))
print("This call will cost",total_cost)