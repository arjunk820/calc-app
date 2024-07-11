import sys

class Calculator:
    def __init__(self) -> None:
        self.numbers = "0123456789"
        self.operators = "+-*x/"
        self.numOne = ""
        self.numTwo = ""
        self.operator = ""
        self.error = False
    
    def getNumbers(self):
        return self.numbers

    def getOperators(self):
        return self.operators

    # Consider negative numbers application
    def stringToInt(self, input):
        if input == "":
            self.error = True

        for c in input:
            if c in self.numbers:
                self.numTwo += c
            elif c in self.operators:
                self.operator += c
                self.numOne = self.numTwo
                if len(self.operator) > 1:
                    self.error = True
        
        if self.numOne == "":
            self.numOne = 0
        else:
            self.numOne = int(self.numOne)
        
        if self.numTwo == "":
            self.numTwo = 0
        else:
            self.numTwo = int(self.numTwo)

        self.doOperation(self)

    def doOperation(self):

        if self.operator == "+":
            self.doAdd(self)
        elif self.operator == "-":
            self.doSubtract(self)
        elif self.operator == "x" or self.operator == "*":
            self.doMultiply(self)
        elif self.operator == "/":
            self.doDivide(self)
        else:
            print("Error: Invalid operator.")
