#Tutorial followed TechWithTim Youtube 9Jan2022

name = input("What is your name Adventurer? ")
print("Welcome to your adventure,",name,"!")

answer = input("You are on a path which has come to an end. You can go left or right. Which way do you want to go? ").lower()

if answer == "left":
    answer = input("You arrive at a river. You can walk up stream, down stream, or swim across. (up/down/swim): ").lower()

    if answer == "swim":
        print("The current is too strong and you were swept down stream.")
    elif answer == "up":
        print("You walk for many miles with no way to cross the river.")
    elif answer == "down":
        print("You arrive at an old bridge across the river. Do you want to cross or walk further?")
    else:
        print("That is not a valid option.")

elif answer == "right":
    print("The path ends at a cave and a path to the left. Do you enter or go left?")
else:
    print("That is not a vaild option.")

print("Thank you for playing,",name,"!")