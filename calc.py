# This is my .py calculator file. July 11 2024.

import sys
from Calculator import Calculator

# Instance of Calculator class object
calc = Calculator()

nums = calc.getNumbers()
ops = calc.getOperators()

def main():

    print("Hello, welcome to my calculator app! Please enter an operation in the following format: numOne (int) operator (+-*x/) numTwo (int). Enter 'q' to quit the program.")

    # Runs for each operation entered into calculator
    for line in sys.stdin:
        string = ""
        for c in line:
            
            # In the case of suspending the program
            if c == 'q':
                print("Thank you for using the calculator. Goodbye!")
                exit(1)

            # Removes non-numerals and non-operators
            if c in nums or c in ops:
                string += c
        
        flag = False

        # Checks if there is 1 and only 1 operator
        for c in string:
            if c in ops and not flag:
                flag = True
            elif c in ops and flag:
                raise ValueError("Multiple operators detected")
        
        # Checks if the parsed input string is a valid operation
        if string == "" or not flag:
            raise ValueError("Invalid input operation given")
        else:
            calc.parseEquation(string)

if __name__ == '__main__':
    main()