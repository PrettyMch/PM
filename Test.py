print("Hello, Welcome to my calculator")

Name = input("Please enter your name: ")

print("Welcome " + Name + "What would you like to do? ")

Command = input("For addition enter 1, substraction enter 2, division enter 3 and multiplication enter 4")




    
if Command == "1":

        First_Value = input("Please enter the first value :")
        Second_Value = input("Please enter the second value :")

        Addition = int(First_Value) + int(Second_Value)

        print("Your answer is " + str(Addition))

elif Command == "2":

        First_Value = input("Please enter the first value :")
        Second_Value = input("Please enter the second value :")

        Subtraction = int(First_Value) - int(Second_Value)

        print("Your answer is " + str(Subtraction))

elif Command == "3":

        First_Value = input("Please enter the first value :")
        Second_Value = input("Please enter the second value :")

        Division = int(First_Value) / int(Second_Value)

        print("Your answer is " + str(Divsion))

elif Command == "4":

        First_Value = input("Please enter the first value :")
        Second_Value = input("Please enter the second value :")

        Multiplication = int(First_Value) * int(Second_Value)

        print("Your answer is " + str(Multiplication))

else:

        print("Invalid input")



    
    

