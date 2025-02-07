correct_pin = 1234
attempts = 3
import getpass
# add necessary variables
while attempts != 0:
    # create a while loop at the beggining of the code to let the programme know the whole thing must be repeated
    supplied_pin = int(getpass.getpass("Enter your PIN:",))
    # create the input variable
    if supplied_pin == correct_pin:
        # set the first condition, if the input pin is the same as the desired one, meaning correct, return relevant statement to the user
        print("PIN correct")
        break
#         break statement to exit
#     condition for incorrect pin below
    elif supplied_pin != correct_pin:
        attempts = attempts -1
        # telling the programme to reduce the number of attempts by one with each loop/incorrect pin entry
        print("WRONG PIN,remaining attempts:", attempts)
#         message to be returned telling the user their attempt was incorrect and how many they have left
