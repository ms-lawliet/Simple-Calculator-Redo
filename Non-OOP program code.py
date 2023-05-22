# Create a Simple App Calculator

# ask for operation
operation = input("Enter operation to be used: ")
# ask for user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

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

# ask if user wants to retry
retry = input("Do you want to try again? (yes or no) ").lower()
# if yes, repeat process
# if no, print "Thank you!"
