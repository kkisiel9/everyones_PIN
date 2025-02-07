# getpass is a Python module used for securely handling user input (especially passwords or PINs) without displaying them on the screen.
import getpass

correct_pin = "4545"
print(correct_pin)
print(type(correct_pin))
max_attempts = 3

# A for loop iterates over a sequence (list, range, string, etc.)
# and since we know the max attempts, we can use range(max_attempts).
for attempt in range(max_attempts):  # # attempt is a loop variable and 'in' is used to iterate over a range of max_attempts(3).
    # supplied_pin = input("Enter your Pin: ")
    supplied_pin = getpass.getpass("Enter your Pin: ")
    if supplied_pin == correct_pin:
        # An f-string in Python allows embedding variables, operations, and function calls inside placeholder{} for dynamic formatting.
        print(f"Access granted. You succeeded in {attempt + 1} attempt.")
        break  # loop control statement,Exit the loop immediately when the correct PIN is entered
    else:
        print(f"Failed : Access denied,try again with correct pin {max_attempts - attempt - 1} attempts left.")
        # This runs only if the loop finishes completely-all attempts used
else:
    print("Access denied!! You have used all attempts")  # Only prints if the loop completes without `break`

