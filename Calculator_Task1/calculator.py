#!/usr/bin/env python3
"""
Calculator CLI App
A command-line calculator supporting basic mathematical operations.

Author: Calculator App
Date: September 24, 2025
"""

import sys
from typing import Union


class Calculator:
    """A simple calculator class with basic mathematical operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from first number."""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    @staticmethod
    def power(a: float, b: float) -> float:
        """Raise first number to the power of second number."""
        return a ** b
    
    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Get remainder when first number is divided by second number."""
        if b == 0:
            raise ValueError("Cannot perform modulo by zero!")
        return a % b


class CalculatorApp:
    """Main calculator application class."""
    
    def __init__(self):
        self.calculator = Calculator()
        self.operations = {
            '1': ('Addition (+)', self.calculator.add),
            '2': ('Subtraction (-)', self.calculator.subtract),
            '3': ('Multiplication (*)', self.calculator.multiply),
            '4': ('Division (/)', self.calculator.divide),
            '5': ('Power (**)', self.calculator.power),
            '6': ('Modulo (%)', self.calculator.modulo),
        }
    
    def display_menu(self) -> None:
        """Display the calculator menu."""
        print("\n" + "="*50)
        print("           CALCULATOR CLI APP")
        print("="*50)
        print("Select an operation:")
        print("-" * 30)
        
        for key, (description, _) in self.operations.items():
            print(f"{key}. {description}")
        
        print("0. Exit")
        print("="*50)
    
    def get_number_input(self, prompt: str) -> float:
        """Get a valid number input from user."""
        while True:
            try:
                value = input(prompt)
                return float(value)
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
    
    def get_operation_choice(self) -> str:
        """Get a valid operation choice from user."""
        while True:
            choice = input("Enter your choice (0-6): ").strip()
            if choice in ['0'] + list(self.operations.keys()):
                return choice
            print("❌ Invalid choice! Please select a number between 0-6.")
    
    def perform_calculation(self, choice: str) -> None:
        """Perform the selected calculation."""
        if choice == '0':
            return
        
        operation_name, operation_func = self.operations[choice]
        print(f"\n📊 You selected: {operation_name}")
        
        # Get numbers from user
        num1 = self.get_number_input("Enter first number: ")
        num2 = self.get_number_input("Enter second number: ")
        
        try:
            result = operation_func(num1, num2)
            
            # Format the operation symbol for display
            symbol_map = {
                'Addition (+)': '+',
                'Subtraction (-)': '-',
                'Multiplication (*)': '*',
                'Division (/)': '/',
                'Power (**)': '**',
                'Modulo (%)': '%'
            }
            
            symbol = symbol_map[operation_name]
            
            # Display result with proper formatting
            print(f"\n✅ Result: {num1} {symbol} {num2} = {result}")
            
            # Format large numbers and decimals nicely
            if isinstance(result, float) and result.is_integer():
                print(f"✅ Simplified: {int(result)}")
            elif abs(result) >= 1000000:
                print(f"✅ Scientific notation: {result:.2e}")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
    
    def run(self) -> None:
        """Main application loop."""
        print("🔢 Welcome to Calculator CLI App!")
        print("This calculator supports basic mathematical operations.")
        
        while True:
            self.display_menu()
            choice = self.get_operation_choice()
            
            if choice == '0':
                print("\n👋 Thank you for using Calculator CLI App!")
                print("Goodbye! 🔢")
                sys.exit(0)
            
            self.perform_calculation(choice)
            
            # Ask if user wants to continue
            while True:
                continue_choice = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\n👋 Thank you for using Calculator CLI App!")
                    print("Goodbye! 🔢")
                    sys.exit(0)
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no.")


def main():
    """Main entry point of the application."""
    try:
        app = CalculatorApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Calculator interrupted by user. Goodbye! 🔢")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()