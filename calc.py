# This is my .py calculator file

import sys
from Calculator import Calculator

calc = Calculator()

nums = calc.getNumbers()
ops = calc.getOperators()

def main():

    print("Hello, welcome to my calculator app! Please enter an operation in the following format: numOne (int) operator (+-*x/) numTwo (int). Enter 'q' to quit the program.")

    for line in sys.stdin:
        string = ""
        for c in line:
            
            if c == 'q':
                print("Thank you for using the calculator. Goodbye!")
                exit(1)

            if c in nums or c in ops:
                string += c
        
        flag = False
        for c in string:
            if c in ops and not flag:
                flag = True
            elif c in ops and flag:
                raise ValueError("Multiple operators detected")
        
        # Call calculator function
        if string == "" or not flag:
            raise ValueError("Invalid input given")
        else:
            calc.stringToInt(string)

if __name__ == '__main__':
    main()