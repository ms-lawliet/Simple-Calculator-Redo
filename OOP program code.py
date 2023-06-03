# import files
from UserInterface import UserInterface
from ImprovedCalc import ImprovedCalculator

# assign class methods to variables
ui = UserInterface()
calc = ImprovedCalculator()

ui.print_title()

while True:
    # ask for input by calling methods
    operation = ui.ask_operation()
    num1 = ui.ask_num1()
    num2 = ui.ask_num2()

    # create instances for operations
    sum = calc.add(num1, num2)
    difference = calc.subtract(num1, num2)
    product = calc.multiply(num1, num2)
    quotient = calc.divide(num1, num2)
    power = calc.power(num1, num2)
    nth_root = calc.nth_root(num1, num2)

    # call method to print result
    ui.print_result(operation, sum, difference, product, quotient, power, nth_root)

    # call method for retry
    if not ui.retry():
        break
