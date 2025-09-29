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