"""
Calculator module containing basic arithmetic operations.
"""

class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        """Raise first number to the power of second number."""
        return a ** b
    
    def square_root(self, a):
        """Calculate square root of a number."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return a ** 0.5
    
    def percentage(self, a, b):
        """Calculate percentage: a% of b."""
        return (a / 100) * b