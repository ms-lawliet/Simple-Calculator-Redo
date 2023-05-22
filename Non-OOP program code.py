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
# for division,
# ask if user wants to retry
# if yes, repeat process
# if no, print "Thank you!"
