"""
Configuration settings for the calculator app.
"""

# Application settings
APP_NAME = "Python Calculator"
APP_VERSION = "1.0.0"

# History settings
HISTORY_FILE = "calculation_history.json"
MAX_HISTORY_ENTRIES = 100

# Display settings
WELCOME_WIDTH = 50
MENU_WIDTH = 40
RESULT_WIDTH = 30

# Supported operations
OPERATIONS = {
    '+': 'Addition',
    '-': 'Subtraction',
    '*': 'Multiplication',
    '/': 'Division',
    '**': 'Power/Exponentiation',
    'sqrt': 'Square Root',
    '%': 'Percentage'
}

# Error messages
ERROR_MESSAGES = {
    'invalid_number': "Please enter a valid number.",
    'invalid_operation': "Please enter a valid operation.",
    'division_by_zero': "Cannot divide by zero!",
    'negative_sqrt': "Cannot calculate square root of negative number!",
    'file_error': "Error accessing file.",
    'unexpected_error': "An unexpected error occurred."
}