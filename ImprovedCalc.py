from SimpleCalc import SimpleCalculator
from colorama import Fore, Back, Style


class ImprovedCalculator(SimpleCalculator):
    def power(self, num1, num2):
        try:
            power = num1 ** num2
            return power
        except TypeError:
            return Fore.RED + Back.RESET + Style.BRIGHT + "Cannot perform operation due to invalid input."
