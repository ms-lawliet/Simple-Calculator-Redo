# import files
from UserInterface import UserInterface
from SimpleCalc import SimpleCalculator

# assign class methods to variables
ui = UserInterface()
calc = SimpleCalculator()

# ask for input by calling methods
operation = ui.ask_operation()
num1 = ui.ask_num1()
num2 = ui.ask_num2()

# create instances for operations
sum = calc.add(num1, num2)
difference = calc.subtract(num1, num2)
product = calc.multiply(num1, num2)
quotient = calc.divide(num1, num2)

# call method to print result
ui.print_result(operation, sum, difference, product, quotient)

# call method for retry
