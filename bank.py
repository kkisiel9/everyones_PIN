import getpass
# I have imported the getpass module from the python package
bank_pin = "1111"

count = 0
# I have included a count variable and assigned it to 0. This will allow me to increment it
while count < 3:
 # I have included a while loop
    supplied_pin = getpass.getpass("Enter your PIN: ",None)
    if supplied_pin == bank_pin:
         print("Successful PIN")
         break
    else:
     count += 1
    #I have created an incrementer of 1 which will cycle the loop if the condition is not met
     print("PIN incorrect")
print("You've used too many attempts")





