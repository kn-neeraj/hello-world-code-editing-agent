# Python Calculator App

A modular calculator application built with Python that provides basic arithmetic operations with a user-friendly interface and calculation history.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power/exponentiation, square root, percentage calculations
- **Calculation History**: Automatic saving and viewing of calculation history
- **Input Validation**: Robust input validation with error handling
- **Modular Design**: Well-organized code structure with separate modules
- **Persistent Storage**: History saved to JSON file for persistence across sessions

## File Structure

```
sample_calculator_app/
├── main.py                 # Application entry point
├── calculator_app.py       # Main application logic
├── calculator.py           # Core calculation operations
├── input_validator.py      # Input validation functions
├── display.py              # User interface display functions
├── history.py              # Calculation history management
├── config.py              # Configuration settings
├── test_calculator.py      # Unit tests
└── README.md              # This file
```

## Installation and Usage

1. **Navigate to the calculator directory**:
   ```bash
   cd sample_calculator_app
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

## Supported Operations

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Addition | + | Add two numbers |
| Subtraction | - | Subtract second number from first |
| Multiplication | * | Multiply two numbers |
| Division | / | Divide first number by second |
| Power | ** | Raise first number to power of second |
| Square Root | sqrt | Calculate square root (single operand) |
| Percentage | % | Calculate a% of b |

## Usage Examples

### Basic Calculations
```
Enter operation: +
Enter first number: 10
Enter second number: 5
Result: 10 + 5 = 15
```

### Square Root
```
Enter operation: sqrt
Enter number: 25
Result: √25 = 5.0
```

### Percentage
```
Enter operation: %
Enter first number: 20
Enter second number: 150
Result: 20% of 150 = 30.0
```

## Menu Options

1. **Perform calculation** - Execute arithmetic operations
2. **View calculation history** - Display all previous calculations
3. **Clear history** - Remove all calculation history
4. **Exit** - Close the application

## Error Handling

The application includes comprehensive error handling for:
- Invalid number inputs
- Division by zero
- Square root of negative numbers
- Unsupported operations
- File I/O errors

## Testing

Run the unit tests to verify calculator functionality:
```bash
python test_calculator.py
```

## History Management

- Calculations are automatically saved with timestamps
- History persists between application sessions
- History is stored in `calculation_history.json`
- Users can view and clear history through the menu

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: None (uses only standard library)
- **Storage**: JSON file format for history
- **Architecture**: Object-oriented with modular design
- **Error Handling**: Exception handling with user-friendly messages

## Contributing

To extend the calculator:

1. Add new operations to `calculator.py`
2. Update `input_validator.py` for new operation validation
3. Modify `display.py` for new operation display
4. Add corresponding tests to `test_calculator.py`
5. Update configuration in `config.py`

## License

This project is open source and available under the MIT License.