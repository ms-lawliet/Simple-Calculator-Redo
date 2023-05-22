class UserInterface:
    def ask_operation(self):
        # ask for operation
        operation = input("Which operation do you want to perform? ").lower()
        return operation

    def ask_num1(self):
        # ask for user input
        num1 = float(input("Enter first number: "))
        return num1

    def ask_num2(self):
        # ask for user input
        num2 = float(input("Enter second number: "))
        return num2

    # display result based on chosen operation
    def print_result(self, operation, sum, difference, product, quotient):
        if operation == "addition":
            print(f"The sum is {sum}.")
        elif operation == "subtraction":
            print(f"The difference is {difference}.")
        elif operation == "multiplication":
            print(f"The product is {product}.")
        elif operation == "division":
            print(f"The quotient is {quotient}.")
        else:
            print("Invalid operation. Try again.")

    # ask if user wants to retry
    # if yes, repeat process
    # if no, print "Thank you!"
