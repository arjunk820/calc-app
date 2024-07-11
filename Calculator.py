import sys

# This is the calculator class I created
class Calculator:

    # Constructor
    def __init__(self) -> None:
        self.numbers = "0123456789"
        self.operators = "+-*x/"
        self.numOne = ""
        self.numTwo = ""
        self.operator = "+"
        self.error = False
    
    def getNumbers(self):
        return self.numbers

    def getOperators(self):
        return self.operators

    # Parses the operation into numbers and operators
    def parseEquation(self, input):
        
        for c in input:
            if c in self.operators:
                self.operator = c
                self.numOne = self.numTwo
                self.numTwo = ""
            else:
                self.numTwo += c

        self.doOperation(int(self.numOne), int(self.numTwo), self.operator)

    # Determines which operation to use
    def doOperation(self, numOne, numTwo, op):

        res = 0
        if op == "+":
            res = self.doAdd(numOne, numTwo)
        elif op == "-":
            res = self.doSubtract(numOne, numTwo)
        elif op == 'x' or op == '*':
            res = self.doMultiply(numOne, numTwo)
        elif op == "/":
            res = self.doDivide(numOne, numTwo)
        print(res)
        self.numOne, numOne, self.numTwo, numTwo = "", 0, "", 0
        
    def doAdd(self, numOne, numTwo):
        return (numOne + numTwo)

    def doSubtract(self, numOne, numTwo):
        return (numOne - numTwo)
    
    def doMultiply(self, numOne, numTwo):
        return (numOne * numTwo)

    def doDivide(self, numOne, numTwo):
        return (numOne / numTwo) if numTwo != 0 else 0