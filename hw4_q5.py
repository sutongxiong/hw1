"""
Author: Sutong Xiong
Assignment / Part: HW4 - Q5
Date due: 2022-10-13, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

total_players = int(input("Enter a valid number of players: "))
while total_players<2 or total_players > 8 :
    total_players = int(input("Enter a valid number of players: "))
highest_sum = 0.0
richest_player = 0
for player_number in range(1,total_players+1):
    total_property_value = 0.0

    property_value = input("Enter the value of a property/asset, or DONE to finish: ")
    while property_value != "DONE":

        total_property_value += float(property_value)
        property_value = input("Enter the value of a property/asset, or DONE to finish: ")
    print("Player", player_number, "has", round(total_property_value,2), "dollars")
    if highest_sum < total_property_value:
        highest_sum = round(total_property_value,2)
        richest_player = player_number

print(richest_player, "wins with",highest_sum, "dollars!")
