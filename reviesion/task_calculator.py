class Calculator:

    def sum(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return False

        #  if b:
        #     return a / b
        #  return False


calc = Calculator()
print(calc.sum(1, 3))
print(calc.divide(1, 0))
