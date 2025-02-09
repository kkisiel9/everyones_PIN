import sys, glob, os
import getpass
# hardcoding the true pin by assigning a string to a variable
pin = "cat"
# setting the number of attempts by assigning it to a variable
attempts = 3
# for attempts from 1 to attempts+1, which will include the 3
for attempt in range(1, attempts+1):
    # prompting to input the pin and assigning the entered pin to a variable
    supplied_pin = getpass.getpass("Enter your PIN: ")
    # if the supplied pin is the same as the real pin
    # printing an appropriate prompt and exiting the loop through break
    if supplied_pin == pin:
        print("Correct password, unlocking your account")
        break
    # if pin is incorrect printing a prompt to ask for another input, and printing the number of the attempt through an f string
    else:
        print(f"Incorrect attempt {attempt}. Try again.")
# when the number of attempts exceeds 3, the code will exit the loop and print a statement that log out failed
else:
    print("Too many incorrect attempts. Log in failed")