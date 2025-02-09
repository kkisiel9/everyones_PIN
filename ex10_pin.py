# Hardcoded PIN
correct_pin = "1234"  # the pin they must enter

# Maximum allowed attempts
max_attempts = 3

# Attempt counter to track how many times the user has entered a PIN
attempts = 0 # Initially set to 0 since no attempts have been made yet

# loop runs as long as the attempt number is below 3 (maximum)
while attempts < max_attempts:
    supplied_pin = input("Enter your PIN: ")   # prompts user to enter pin
    attempts += 1  # Increase attempt count by 1

    # Check if the entered PIN matches the correct PIN
    if supplied_pin == correct_pin:
        print(f"Access granted! You entered the correct PIN in {attempts} attempt(s).")
        break # Exit the loop since the correct PIN was entered
    else:
        # Inform  user that the PIN was incorrect and show the attempt number
        print(f"Incorrect PIN. Attempt {attempts} of {max_attempts}.")

    # If the maximum number of attempts is reached, deny access
    if attempts == max_attempts:
        print("Too many failed attempts. Access denied.") # Final message after 3 incorrect tries
