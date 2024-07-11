# This is my .py calculator file

import sys
from Calculator import Calculator

NUMBERS = "0123456789"
OPERATORS = "+-*/"

def main():
    for line in sys.stdin:
        string = ""
        for c in line:
            if c in NUMBERS or c in OPERATORS:
                string += c
        
        # Call calculator function
        Calculator.stringToInt(string)

if __name__ == '__main__':
    main()