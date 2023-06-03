import time
import pyfiglet
from colorama import Fore, Back, Style


class UserInterface:
    def print_title(self):
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "+-*/" * 185)
        print(Back.BLACK + pyfiglet.figlet_format('Simple Calculator', font='nancyj', width=185, justify='center'),
              end='')
        print(Back.RESET + "+-*/" * 185)
        time.sleep(0.5)

    def ask_operation(self):
        # ask for operation
        operation = input(Fore.LIGHTCYAN_EX + Back.BLACK + Style.BRIGHT + "Which operation do you want to perform? ").lower()
        return operation

    def ask_num1(self):
        # ask for user input
        try:
            num1 = float(input(Back.BLACK + "Enter first number: "))
            return num1
        except ValueError:
            return

    def ask_num2(self):
        # ask for user input
        try:
            num2 = float(input(Back.BLACK + "Enter second number: "))
            return num2
        except ValueError:
            return

    # display result based on chosen operation
    def print_result(self, operation, sum, difference, product, quotient, power):
        if operation == "addition":
            print(Fore.YELLOW + Back.RESET + Style.BRIGHT + str(sum))
        elif operation == "subtraction":
            print(Fore.GREEN + Back.RESET + Style.BRIGHT + str(difference))
        elif operation == "multiplication":
            print(Fore.BLUE + Back.RESET + Style.BRIGHT + str(product))
        elif operation == "division":
            print(Fore.CYAN + Back.RESET + Style.BRIGHT + str(quotient))
        elif operation == "power":
            print(Fore.YELLOW + Back.RESET + Style.BRIGHT + str(power))
        else:
            print(Fore.MAGENTA + Back.RESET + Style.BRIGHT + "Invalid operation. Try again.")

    def retry(self):
        # ask if user wants to retry
        retry = input(Fore.RESET + Back.BLACK + Style.BRIGHT + "Would you like to retry? ").lower()
        # if yes, repeat process
        if retry == "yes":
            return True
        # if no, print "Thank you"
        elif retry == "no":
            print(Fore.LIGHTCYAN_EX + Back.RESET + Style.BRIGHT + "Thank you!")
            return False
        else:
            print(Fore.LIGHTCYAN_EX + Back.RESET + Style.BRIGHT + "Yes or no only.")
