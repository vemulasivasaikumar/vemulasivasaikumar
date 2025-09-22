class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
calc = Calculator(a, b)
if operation == "add":
    result = calc.add()
elif operation == "subtract":
    result = calc.subtract()
elif operation == "multiply":
    result = calc.multiply()
elif operation == "divide":
    result = calc.divide()
else:
    result = "Invalid operation!"

print("Result:", result)
