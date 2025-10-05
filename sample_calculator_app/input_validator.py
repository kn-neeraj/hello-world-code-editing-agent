"""
Input validation module for the calculator app.
"""

def validate_number_input(user_input):
    """
    Validate if the user input is a valid number.
    
    Args:
        user_input (str): The input string from user
        
    Returns:
        float: The validated number
        
    Raises:
        ValueError: If input is not a valid number
    """
    try:
        return float(user_input.strip())
    except ValueError:
        raise ValueError(f"'{user_input}' is not a valid number!")

def validate_operation(operation):
    """
    Validate if the operation is supported.
    
    Args:
        operation (str): The operation symbol
        
    Returns:
        str: The validated operation
        
    Raises:
        ValueError: If operation is not supported
    """
    valid_operations = ['+', '-', '*', '/', '**', 'sqrt', '%']
    operation = operation.strip().lower()
    
    if operation not in valid_operations:
        raise ValueError(f"'{operation}' is not a supported operation!")
    
    return operation

def get_valid_number_input(prompt):
    """
    Get a valid number input from user with retry logic.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        float: The validated number
    """
    while True:
        try:
            user_input = input(prompt)
            return validate_number_input(user_input)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

def get_valid_operation_input():
    """
    Get a valid operation input from user with retry logic.
    
    Returns:
        str: The validated operation
    """
    while True:
        try:
            print("\nSupported operations: +, -, *, /, ** (power), sqrt, % (percentage)")
            operation = input("Enter operation: ")
            return validate_operation(operation)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")