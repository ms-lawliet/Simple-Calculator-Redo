from SimpleCalc import SimpleCalculator
from colorama import Fore, Back, Style


class ImprovedCalculator(SimpleCalculator):
    # for division
    def divide(self, num1, num2):
        try:
            quotient = round(num1 / num2, 2)
            return quotient
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."
        except ZeroDivisionError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Zero Division Error."

    # for power
    def power(self, num1, num2):   # raise num1 to the power of num2
        try:
            power = num1 ** num2
            return power
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."

    # for nth_root
    def nth_root(self, num1, num2):    # find the square root, cube root, fourth root, etc.
        try:
            nth_root = num1 ** (1/num2)  # num2 represents the nth root
            return nth_root
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."
