class UserInterface:
    def ask_operation(self):
        # ask for operation
        operation = input("Which operation do you want to perform? ").lower()
        return operation

    def ask_num1(self):
        # ask for user input
        try:
            num1 = float(input("Enter first number: "))
            return num1
        except ValueError:
            return "Invalid input."

    def ask_num2(self):
        # ask for user input
        try:
            num2 = float(input("Enter second number: "))
            return num2
        except ValueError:
            return "Invalid input."

    # display result based on chosen operation
    def print_result(self, operation, sum, difference, product, quotient):
        if operation == "addition":
            print(f"The sum is {sum}")
        elif operation == "subtraction":
            print(f"The difference is {difference}")
        elif operation == "multiplication":
            print(f"The product is {product}")
        elif operation == "division":
            print(f"The quotient is {quotient}")
        else:
            print("Invalid operation. Try again.")

    def retry(self):
        # ask if user wants to retry
        retry = input("Would you like to retry? ").lower()
        # if yes, repeat process
        if retry == "yes":
            return True
        # if no, print "Thank you"
        elif retry == "no":
            print("Thank you!")
            return False
        else:
            print("Yes or no only.")
