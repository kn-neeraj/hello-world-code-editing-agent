# Hello World Code Editing Agent

Building a conversational coding agent using Claude Tool Calling feature. The agent runs a continuous conversation loop where: 
- Define tool defintiions list_files, file_read, edit_file
- Create claude client with above tool defintions
- Claude decides to use any of the tools to sovle the task
- Claude formulates a response 
- Loop continous 

This repo is based on this blog https://ampcode.com/how-to-build-an-agent. The blog implemented in Go, we implemented on Python.

### Uses
- Claude Python Client
- Tool Calling 
- Claude Sonnect 4

### Key Components

- Agent Class : Orchestrates entire conversation flow, manage conversatin history, main conversation loop! 
- 3 Tool Definitions : Tool defintions for `read_file`, `list_files`, and `edit_file`

### Sample Runs

#### Successful Run
Creating a calculator app with 1 prompt where the agent uses available tools along with Claude reasoning in loop.

```
You: Can you create a calculator app in python with multiple files in the folder sample_calculator_app
Claude: I'll create a calculator app in Python with multiple files in the `sample_calculator_app` folder. Let me start by creating the folder structure and then implement the different components.
tool: list_files({"path": "."})
tool: list_files({"path": "sample_calculator_app"})
Claude: I'll create the calculator app with multiple files. Let me start with the main calculator operations module:
tool: edit_file({"path": "sample_calculator_app/calculator.py", "old_str": "", "new_str": "\"\"\"\nCalculator 

.... lots of tool calls...

tool: edit_file({"path": "sample_calculator_app/run_calculator.py", "old_str": "", "new_str": "#!/usr/bin/env python3\n\"\"\"\nSimple script to run the calculator application.\nThis can be used as an alternative to running main.py\n\"\"\"\n\nimport sys\nimport os\n\n# Add the current directory to Python path to ensure imports work\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n\nfrom main import main\n\nif __name__ == \"__main__\":\n    print(\"Starting Python Calculator App...\")\n    print(\"Press Ctrl+C at any time to exit.\\n\")\n    main()"})
Claude: Now let me verify all the files were created correctly:
tool: list_files({"path": "sample_calculator_app"})
Claude: Perfect! I've successfully created a comprehensive calculator app in Python with multiple files in the `sample_calculator_app` folder. Here's what I've built:

## File Structure and Components:

1. **`main.py`** - Entry point for the application
2. **`calculator_app.py`** - Main application logic and user interface flow
3. **`calculator.py`** - Core Calculator class with all arithmetic operations
4. **`input_validator.py`** - Input validation functions with error handling
5. **`display.py`** - All user interface display functions
6. **`history.py`** - Calculation history management with JSON persistence
7. **`config.py`** - Configuration settings and constants
8. **`test_calculator.py`** - Unit tests for the calculator functionality
9. **`README.md`** - Comprehensive documentation
10. **`requirements.txt`** - Dependencies (uses only standard library)
11. **`__init__.py`** - Package initialization
12. **`run_calculator.py`** - Alternative run script

## Key Features:

- **Modular Architecture**: Each component has a specific responsibility
- **Multiple Operations**: Addition, subtraction, multiplication, division, power, square root, percentage
- **Input Validation**: Robust error handling for invalid inputs
- **History Management**: Automatic saving/loading of calculation history with timestamps
- **User-Friendly Interface**: Clear menus and formatted output
- **Persistent Storage**: History saved to JSON file
- **Unit Tests**: Comprehensive test coverage
- **Error Handling**: Graceful handling of edge cases like division by zero
```