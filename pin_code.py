# this is a variable that I have created for the correct pin.
# this pin is a string
correct_pin = "1234"

# this is another variable to show the number of maximum attempts which is an integer.
max_attempts_count = 3

# this variable shows the current amount of attempts
current_attempt_count = 0

# when the current attempt is less than the maximum the attempts get increased by 1 and the input function is shown so you can enter the pin in
while current_attempt_count < max_attempts_count:
    # i have created a variable for the inputted pin
    # input function prompts the user to enter their pin and no need to use print function
    pin_input = input("Enter your PIN: ")
    current_attempt_count += 1

    # if the input number is the same as the actual pint a print message is printed with the number of actual attempts it took.
    # == double equals needs to be used as this is a comparison operator
    # single = just assigns in python
    if pin_input == correct_pin:
        print(f"Access granted! You entered the correct PIN in {current_attempt_count} attempt(s).")
        # break statement ensure this loop keeps running until max attempts is reached
        break
    # this gets printed whe you enter the incorrect pin but are still within the max attempts
    else:
        print(f"Incorrect PIN. Attempt {current_attempt_count}")

    # if the max attempts is exceeded the program print this
    if current_attempt_count == max_attempts_count:
        print("Too many failed attempts. Access denied.")

# this is an example of conditionals where break and its friends are used