"""
History management module for the calculator app.
"""

import json
import os
from datetime import datetime

class CalculationHistory:
    """Class to manage calculation history."""
    
    def __init__(self, history_file="calculation_history.json"):
        """
        Initialize history manager.
        
        Args:
            history_file (str): Path to the history file
        """
        self.history_file = history_file
        self.history = self._load_history()
    
    def _load_history(self):
        """
        Load history from file.
        
        Returns:
            list: List of calculation history entries
        """
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_history(self):
        """Save history to file."""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.history, f, indent=2)
        except IOError:
            print("Warning: Could not save history to file.")
    
    def add_calculation(self, operation, num1, num2, result):
        """
        Add a calculation to history.
        
        Args:
            operation (str): The operation performed
            num1 (float): First number
            num2 (float): Second number (None for single operand operations)
            result (float): The calculation result
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if operation == 'sqrt':
            calculation_str = f"√{num1} = {result}"
        elif operation == '+':
            calculation_str = f"{num1} + {num2} = {result}"
        elif operation == '-':
            calculation_str = f"{num1} - {num2} = {result}"
        elif operation == '*':
            calculation_str = f"{num1} × {num2} = {result}"
        elif operation == '/':
            calculation_str = f"{num1} ÷ {num2} = {result}"
        elif operation == '**':
            calculation_str = f"{num1} ^ {num2} = {result}"
        elif operation == '%':
            calculation_str = f"{num1}% of {num2} = {result}"
        else:
            calculation_str = f"{num1} {operation} {num2} = {result}"
        
        entry = f"[{timestamp}] {calculation_str}"
        self.history.append(entry)
        self._save_history()
    
    def get_history(self):
        """
        Get calculation history.
        
        Returns:
            list: List of calculation history entries
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear all calculation history."""
        self.history = []
        self._save_history()
        if os.path.exists(self.history_file):
            try:
                os.remove(self.history_file)
            except IOError:
                pass
    
    def get_history_count(self):
        """
        Get number of calculations in history.
        
        Returns:
            int: Number of calculations
        """
        return len(self.history)