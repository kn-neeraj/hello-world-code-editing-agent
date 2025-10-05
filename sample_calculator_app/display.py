"""
Display module for the calculator app UI.
"""

def display_welcome():
    """Display welcome message."""
    print("=" * 50)
    print("         PYTHON CALCULATOR APP")
    print("=" * 50)
    print("Welcome to the Python Calculator!")
    print("This calculator supports basic arithmetic operations.")

def display_menu():
    """Display the main menu options."""
    print("\n" + "-" * 40)
    print("CALCULATOR MENU")
    print("-" * 40)
    print("1. Perform calculation")
    print("2. View calculation history")
    print("3. Clear history")
    print("4. Exit")
    print("-" * 40)

def display_operation_help():
    """Display help for available operations."""
    print("\n" + "-" * 40)
    print("AVAILABLE OPERATIONS")
    print("-" * 40)
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("** : Power/Exponentiation")
    print("sqrt : Square root (only requires one number)")
    print("% : Percentage (a% of b)")
    print("-" * 40)

def display_result(operation, num1, num2, result):
    """
    Display calculation result.
    
    Args:
        operation (str): The operation performed
        num1 (float): First number
        num2 (float): Second number (None for single operand operations)
        result (float): The calculation result
    """
    print("\n" + "=" * 30)
    print("CALCULATION RESULT")
    print("=" * 30)
    
    if operation == 'sqrt':
        print(f"√{num1} = {result}")
    elif operation == '+':
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        print(f"{num1} × {num2} = {result}")
    elif operation == '/':
        print(f"{num1} ÷ {num2} = {result}")
    elif operation == '**':
        print(f"{num1} ^ {num2} = {result}")
    elif operation == '%':
        print(f"{num1}% of {num2} = {result}")
    
    print("=" * 30)

def display_history(history):
    """
    Display calculation history.
    
    Args:
        history (list): List of calculation history entries
    """
    print("\n" + "=" * 40)
    print("CALCULATION HISTORY")
    print("=" * 40)
    
    if not history:
        print("No calculations performed yet.")
    else:
        for i, entry in enumerate(history, 1):
            print(f"{i:2d}. {entry}")
    
    print("=" * 40)

def display_error(error_message):
    """
    Display error message.
    
    Args:
        error_message (str): The error message to display
    """
    print("\n" + "!" * 40)
    print("ERROR")
    print("!" * 40)
    print(f"An error occurred: {error_message}")
    print("!" * 40)

def display_goodbye():
    """Display goodbye message."""
    print("\n" + "=" * 50)
    print("Thank you for using Python Calculator!")
    print("Goodbye!")
    print("=" * 50)