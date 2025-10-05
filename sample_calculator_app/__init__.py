"""
Python Calculator App Package

A modular calculator application with multiple arithmetic operations,
input validation, history management, and a user-friendly interface.
"""

__version__ = "1.0.0"
__author__ = "Calculator App Developer"
__email__ = "developer@example.com"

from .calculator import Calculator
from .calculator_app import CalculatorApp
from .history import CalculationHistory

__all__ = ["Calculator", "CalculatorApp", "CalculationHistory"]