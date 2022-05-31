# User runs program
# Ask user for operation type and save/cache it
# Ask user for numbers/floats
# Validate user numbers
# Perfom mathematical operation on usersnumbers and print result
# Ask usr whether s/he'd like to perform an operation
# If yes, restart loop
# Else, break the loop and end the taks
#Ctrl + c to exist any python program

print("Welcome to Simple CLI Calculator")

is_running = True  #the  flag of the while loop, while still writing the code in a while loop before you break use pass

while is_running:
    print("Starting calculator process")
    user_operation = input("What operation would you like to perfrom?\nPick any operation from ['+','-','*','/']") 
    
    try:
        a = float(input("First number = "))
        b = float(input("Second number = "))
    except:
        print("Failed, invalid number")
        continue # continue take us right back to the top!!!

    if user_operation == "+":
        print(a+b)
    elif user_operation == "-":        
        print(a-b)
    elif user_operation == "*":
        print(a*b)
    elif user_operation == "/":
        print(a/b)
    else:
        print("Invalid operation entered, try again...")

        
    choice = input("Would you like to carry out another calculation. y/n")
    if choice == "y":
         pass
    if choice == "n":
        is_running = False # same thing as break
        print("Thank you for using Simple CLI Calculator")
