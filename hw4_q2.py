"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q2
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

n = int(input("Enter the number of lines composed of half of the asterisks: "))
for i in range(1,n+1):
    print(" "*(i-1) + "*"*(2*n-2*i+1)+" "*(i-1))
for i in range(n-1):
    print(" "*(n-i-2) + "*"*(i*2+2*n-5) + " " * (n-i-2))



