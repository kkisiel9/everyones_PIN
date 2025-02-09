
correct_pin = "1234"


max_attempts = 3


attempts = 0

while attempts < max_attempts:
    supplied_pin = input("Enter your PIN: ")
    attempts += 1  # Increase attempt count

    if supplied_pin == correct_pin:
        print(f"Access granted! You entered the correct PIN in {attempts} attempt(s).")
        break
    else:
        print(f"Incorrect PIN. Attempt {attempts} of {max_attempts}.")

    if attempts == max_attempts:
        print("Too many failed attempts. Access denied.")
