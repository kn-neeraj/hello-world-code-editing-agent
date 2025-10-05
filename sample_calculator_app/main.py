"""
Entry point for the calculator application.
"""

from calculator_app import CalculatorApp

def main():
    """Main function to start the calculator app."""
    try:
        app = CalculatorApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please restart the application.")

if __name__ == "__main__":
    main()