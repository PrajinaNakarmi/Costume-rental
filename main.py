import rent #importing from rent.py
import return1 #importing from return1.py
import message #importing message for selectoption
import exitfile #importing from exitfile
#title of the application
print("-------------------------------------------------------------------")
print("*******************************************************************")
print("                 Welcome to costume rental application            ")
print("*******************************************************************")
print("-------------------------------------------------------------------")

loop = True

while loop == True:

    message.selectOption() #importing from message
    s = True
    while s == True:

        try:
            select = int(input("Enter a option: "))
            s = False
        except ValueError:
                print("\n******************************************************")
                print("                   Invalid Input                     ")
                print("******************************************************\n")
            
    if select == 1:
        rent.rent() #importing from rent.py

    elif select == 2:
        return1.Return() #importing from return1.py

    elif select == 3:
        exitfile.exit() #importing from exitfile
        loop = False

    else:
        print("\n******************************************************")
        print("              Choose the valid option!!              ")
        print("******************************************************\n")
