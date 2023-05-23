class SimpleCalculator:
    # perform operation
    # for addition,
    def add(self, num1, num2):
        try:
            sum = num1 + num2
            return sum
        except TypeError:
            return "Cannot perform operation due to invalid input."

    # for subtraction,
    def subtract(self, num1, num2):
        try:
            difference = num1 - num2
            return difference
        except TypeError:
            return "Cannot perform operation due to invalid input."

    # for multiplication,
    def multiply(self, num1, num2):
        try:
            product = num1 * num2
            return product
        except TypeError:
            return "Cannot perform operation due to invalid input."

    # for division,
    def divide(self, num1, num2):
        try:
            quotient = num1 / num2
            return quotient
        except TypeError:
            return "Cannot perform operation due to invalid input."
        except ZeroDivisionError:
            return "Zero Division Error."
