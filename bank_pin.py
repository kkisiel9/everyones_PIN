import getpass
# we imported this module to hide the input when inserting the PIN
correct_pin = 9999
#  variable 'correct pin' is the value assigned for the correct pin and it is an integer
attempt = 3
# we set a variable for establish the number of attempts that user is allowed to try to enter the pin

while attempt > 0 :
    # we utilise the WHILE loop when we don't know how many times we want to repeat the condition so it continues until the condition is met
    (supplied_pin) = getpass.getpass("Please enter your pin: ", None)
    #as expected we get "GetPassWarning" as pycharm doesn't handle secure password input correctly
    if correct_pin ==  int(supplied_pin) :
          # made the value supplied_pin an integer to be able to be able to run the conditional
         # if is expected the statement is true
        print("Correct pin, welcome")
        break
 #        exits the loop
    else:
     attempt -= 1
   # else expect that is statement is false.
    print('incorrect pin, try again')
if attempt == 0 :
    print('Too many attempts access blocked')

