# Create a Simple App Calculator

while True:
    # ask for operation
    operation = input("Enter operation to be used: ").lower()
    try:
        # ask for user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input.")

    try:
        # perform operation
        # for addition,
        if operation == "addition":
            sum = num1 + num2
            print(f"The sum is {sum}.")
        # for subtraction,
        elif operation == "subtraction":
            difference = num1 - num2
            print(f"The difference is {difference}.")
        # for multiplication,
        elif operation == "multiplication":
            product = num1 * num2
            print(f"The product is {product}.")
        # for division,
        elif operation == "division":
            quotient = num1 / num2
            print(f"The quotient is {quotient}.")
        # else, invalid operation
        else:
            print("Operation is invalid.")
    except TypeError:
        print("Cannot perform operation due to invalid input.")
    except NameError:
        print("Cannot perform operation due to invalid input.")
    except ZeroDivisionError:
        print("Zero Division Error.")

    # ask if user wants to retry
    retry = input("Do you want to try again? (yes or no) ").lower()
    # if yes, repeat process
    if retry == "yes":
        continue
    # if no, print "Thank you!"
    elif retry == "no":
        print("Thank you!")
        break
    else:
        print("Yes or no only.")
