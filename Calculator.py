import sys

class Calculator:
    def __init__(self) -> None:
        self.numbers = "0123456789"
        self.operators = "+-*/"

    def stringToInt(self, input):
        if input == "":
            sys.stderr("Error: Invalid input given.")

        numOne = ""

        for c in input:
            if c in self.numbers:
                numOne += c

        return ""