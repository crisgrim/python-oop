class Calculator():
    def __init__(self, a, b):
        print(self.sum(a, b))
        print(self.rest(a, b))
        print(self.multiply(a, b))
        print(self.divide(a, b))

    def sum(self, a, b):
        return a + b

    def rest(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator(5,5)
