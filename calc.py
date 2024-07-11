# This is my .py calculator file

import sys
from Calculator import Calculator

calc = Calculator()

nums = calc.getNumbers()
ops = calc.getOperators()

def main():
    for line in sys.stdin:
        string = ""
        for c in line:
            if c in nums or c in ops:
                string += c
        
        # Call calculator function
        if string == "":
            print("Error: Invalid input")
            break
        else:
            calc.stringToInt(string)

if __name__ == '__main__':
    main()