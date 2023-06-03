from SimpleCalc import SimpleCalculator
from colorama import Fore, Back, Style


class ImprovedCalculator(SimpleCalculator):
    def power(self, num1, num2):   # raise num1 to the power of num2
        try:
            power = num1 ** num2
            return power
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."

    def nth_root(self, num1, num2):    # find the square root, cube root, fourth root, etc.
        try:
            nth_root = num1 ** (1/num2)  # num2 represents the nth root
            return nth_root
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."
