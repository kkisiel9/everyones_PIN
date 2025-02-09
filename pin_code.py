# this is a variable that I have created for the correct pin.
# this pin is a string
correct_pin = "1234"

# this is another variable to show the number of maximum attempts which is an integer.
max_attempts = 3

# this variable shows the current amount of attempts
attempts = 0

# when the current attempt is less than the maximum the attempts get increased by 1 and the input function is shown so you can enter the pin in
while attempts < max_attempts:
    # this uses the input function and also creates a variable for the inputted pin number
    supplied_pin = input("Enter your PIN: ")
    attempts += 1

    # if the input number is the same as the actual pint a print message is printed with the number of actual attempts it took.
    if supplied_pin == correct_pin:
        print(f"Access granted! You entered the correct PIN in {attempts} attempt(s).")
        # break statement ensure this loop keeps running until max attempts is reached
        break
    else:
        print(f"Incorrect PIN. Attempt {attempts}")

    # if the max attempts is exceeded it print this
    if attempts == max_attempts:
        print("Too many failed attempts. Access denied.")

# this is an example of conditionals where break and its friends are used