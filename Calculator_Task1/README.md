# Calculator CLI App 🔢

A command-line calculator application built with Python that supports basic mathematical operations with a user-friendly interface.

## Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Operations**: Power (exponentiation), Modulo
- **Error Handling**: Division by zero protection and input validation
- **User-Friendly**: Clear menu system and interactive prompts
- **Continuous Usage**: Loop until user chooses to exit
- **Professional Output**: Formatted results with emojis and clear messaging

## Project Structure

```
calculator.py          # Main calculator application
README.md             # This documentation file
```

## Code Architecture

The application follows a well-structured object-oriented design:

### Classes

1. **Calculator Class**
   - Contains static methods for mathematical operations
   - Each operation is a separate function (+, -, *, /, **, %)
   - Includes proper error handling (e.g., division by zero)

2. **CalculatorApp Class**
   - Main application logic and user interface
   - Menu display and user input handling
   - Operation selection and execution
   - Continuous loop management

### Key Functions

- `add(a, b)` - Addition operation
- `subtract(a, b)` - Subtraction operation
- `multiply(a, b)` - Multiplication operation
- `divide(a, b)` - Division operation with zero-check
- `power(a, b)` - Exponentiation operation
- `modulo(a, b)` - Modulo operation with zero-check

## Usage

### Running the Calculator

```bash
python calculator.py
```

### Menu Options

```
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (**)
6. Modulo (%)
0. Exit
```

### Example Usage

```
Enter your choice (0-6): 1
📊 You selected: Addition (+)
Enter first number: 15
Enter second number: 25
✅ Result: 15.0 + 25.0 = 40.0
✅ Simplified: 40
```

## Error Handling

- **Invalid Input**: Non-numeric inputs are caught and user is prompted again
- **Division by Zero**: Prevents division and modulo by zero with clear error messages
- **Menu Selection**: Invalid menu choices are handled gracefully
- **Keyboard Interrupt**: Ctrl+C is handled to exit gracefully

## Features Implemented

✅ **Functions for each operation** - Separate methods for +, -, *, /, **, %  
✅ **User input using input()** - Interactive prompts for numbers and operations  
✅ **Loop until user chooses to exit** - Continuous operation with exit option  
✅ **Well-structured schema** - Object-oriented design with proper separation of concerns  

## Additional Features

- 🎨 **Visual Enhancements**: Emojis and formatted output
- 🔄 **Continuous Operation**: Option to perform multiple calculations
- 📊 **Result Formatting**: Scientific notation for large numbers
- 🛡️ **Robust Error Handling**: Comprehensive input validation
- 📝 **Clear Documentation**: Inline comments and docstrings

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone or download the `calculator.py` file
2. Ensure Python 3.6+ is installed
3. Run the application using `python calculator.py`

## Contributing

Feel free to enhance the calculator by adding more mathematical operations or improving the user interface.

## License

This project is open source and available under the MIT License.