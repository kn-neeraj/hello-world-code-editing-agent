"""
Main calculator application module.
"""

from calculator import Calculator
from input_validator import get_valid_number_input, get_valid_operation_input
from display import (
    display_welcome, display_menu, display_operation_help,
    display_result, display_history, display_error, display_goodbye
)
from history import CalculationHistory

class CalculatorApp:
    """Main calculator application class."""
    
    def __init__(self):
        """Initialize the calculator app."""
        self.calculator = Calculator()
        self.history_manager = CalculationHistory()
        self.running = True
    
    def perform_calculation(self):
        """Perform a single calculation."""
        try:
            display_operation_help()
            operation = get_valid_operation_input()
            
            if operation == 'sqrt':
                num1 = get_valid_number_input("Enter number: ")
                result = self.calculator.square_root(num1)
                display_result(operation, num1, None, result)
                self.history_manager.add_calculation(operation, num1, None, result)
            else:
                num1 = get_valid_number_input("Enter first number: ")
                num2 = get_valid_number_input("Enter second number: ")
                
                if operation == '+':
                    result = self.calculator.add(num1, num2)
                elif operation == '-':
                    result = self.calculator.subtract(num1, num2)
                elif operation == '*':
                    result = self.calculator.multiply(num1, num2)
                elif operation == '/':
                    result = self.calculator.divide(num1, num2)
                elif operation == '**':
                    result = self.calculator.power(num1, num2)
                elif operation == '%':
                    result = self.calculator.percentage(num1, num2)
                
                display_result(operation, num1, num2, result)
                self.history_manager.add_calculation(operation, num1, num2, result)
        
        except ValueError as e:
            display_error(str(e))
        except Exception as e:
            display_error(f"Unexpected error: {str(e)}")
    
    def show_history(self):
        """Display calculation history."""
        history = self.history_manager.get_history()
        display_history(history)
    
    def clear_history(self):
        """Clear calculation history."""
        self.history_manager.clear_history()
        print("\nHistory cleared successfully!")
    
    def get_menu_choice(self):
        """
        Get menu choice from user.
        
        Returns:
            int: User's menu choice
        """
        while True:
            try:
                choice = input("\nEnter your choice (1-4): ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= 4:
                    return choice_num
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
    
    def run(self):
        """Run the calculator application."""
        display_welcome()
        
        while self.running:
            display_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.perform_calculation()
            elif choice == 2:
                self.show_history()
            elif choice == 3:
                self.clear_history()
            elif choice == 4:
                self.running = False
                display_goodbye()
            
            if self.running:
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()