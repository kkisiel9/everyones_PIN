import getpass
import sys
from getpass import getpass

required_pin = 8877
# The pin that the user needs to input

supplied_pin = int(input("Please enter your pin.."))
# The int function is so the programme registers an integer for a response
# The input function is to allow the user to type in an answer into the terminal
# the string 'Please enter pin' is what will be displayed/is the prompt for the user to answer

# Attempting question 3
password = getpass('Your pin code please',None)

max_attempt = 3
# This variable represents the maximum amount of times the user can try the pin

attempt_number = 1
# This variable represents the current attempt number the user is on
# It has started at one to account for the program counting from 0

while required_pin != supplied_pin:
    # it is a while loop
    # shebang means not equal to
    attempt_number = attempt_number + 1
    # If the user gets the incorrect pin, it will increase the attempt number by one

    if attempt_number > max_attempt:
        #  if the attempt number is greater than max attempt
        print("Three failed attempts: ACCESS DENIED")
        # This will print if the attempt number is greater then the max attempt
        # The user will no longer be able to have an opportunity to type the pin again
        break
    #     is a loop control statement
    #  helps to terminate the loop

    # Breaks friend in python is continue.
    #continue forces the next iteration of the loop to be executed


    supplied_pin = int(input(f"Incorrect attempt.Please try again."))
#     This is separate from the above if statement
#  This has to go after line 22 otherwise the user will be able to have a 4th attempt

if required_pin == supplied_pin:
    # double '=' means equals to
    print("Successful!")
    #  if the required pin is the same as the supplied pin then the program will print 'Successful"
    # This then completes the while loop as the condition has been met