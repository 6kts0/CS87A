import math
import random


# USER-DEFINED FUNCTIONS: All calculator operations are defined here

def add(a, b):
    """OPERATORS: Addition using + operator"""
    return a + b

def subtract(a, b):
    """OPERATORS: Subtraction using - operator"""
    return a - b

def multiply(a, b):
    """OPERATORS: Multiplication using * operator"""
    return a * b

def divide(a, b):
    """OPERATORS: Division using / operator"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def exponent(a, b):
    """OPERATORS: Exponentiation using ** operator"""
    return a ** b

def square_root(a):
    """MATH LIBRARY: Using math.sqrt() function"""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number!")
    return math.sqrt(a)

def sine(a):
    """MATH LIBRARY: Using math.sin() function (input in radians)"""
    return math.sin(a)

def cosine(a):
    """MATH LIBRARY: Using math.cos() function (input in radians)"""
    return math.cos(a)

def tangent(a):
    """MATH LIBRARY: Using math.tan() function (input in radians)"""
    return math.tan(a)


"""
USER INTERFACE: Displays menu options to user using a LOOP/ITERATOR
This function creates a visual menu using string formatting and iteration
"""
def display_menu():
    print("\n" + "="*50)
    print("            PYTHON CALCULATOR")
    print("="*50)
    
    # LOOPS/ITERATORS: Using a loop to display menu options
    operations = [
        ("1", "Addition (+)"),
        ("2", "Subtraction (-)"),
        ("3", "Multiplication (*)"),
        ("4", "Division (/)"),
        ("5", "Exponent (**)"),
        ("6", "Square Root"),
        ("7", "Sine (radians)"),
        ("8", "Cosine (radians)"),
        ("9", "Tangent (radians)"),
        ("0", "Exit")
    ]
    
    # LOOPS/ITERATORS: Iterating through operations to display them
    for choice, operation in operations:
        print(f"  {choice}. {operation}")
    
    print("="*50 + "\n")



"""
Main calculator function with LOOPS/ITERATORS for continuous operation
"""
def main():
    # LOOPS/ITERATORS: Infinite loop that continues until user exits
    while True:
        display_menu()
        
        # INPUT HANDLING: Get user choice
        try:
            choice = input("Enter your choice (0-9): ").strip()
            
            # INPUT HANDLING: Validate choice is in valid range
            if choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print("Invalid choice! Please enter a number between 0 and 9.")
                continue
            
            # Exit condition
            if choice == '0':
                print("Thank you for using the calculator! Goodbye!")
                break
            
            # Handle square root (only needs one input)
            if choice == '6':
                try:
                    num = float(input("Enter a number: "))
                    result = square_root(num)
                    print(f"Result: {num} = {result}\n")
                except ValueError as ve:
                    print(f"Error: {ve}\n")
                continue
            
            # All other operations need two inputs
            # INPUT HANDLING: Get first number
            try:
                num1 = float(input("Enter first number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
                continue
            
            # INPUT HANDLING: Get second number
            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")
                continue
            
            # OPERATORS & CONDITIONAL LOGIC: Perform calculation based on choice
            result = None
            operation_name = ""
            
            if choice == '1':
                result = add(num1, num2)
                operation_name = f"{num1} + {num2}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation_name = f"{num1} - {num2}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation_name = f"{num1} × {num2}"
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    operation_name = f"{num1} ÷ {num2}"
                except ValueError as ve:
                    print(f"Error: {ve}\n")
                    continue
            elif choice == '5':
                result = exponent(num1, num2)
                operation_name = f"{num1} ^ {num2}"
            elif choice == '7':
                result = sine(num1)
                operation_name = f"sin({num1})"
            elif choice == '8':
                result = cosine(num1)
                operation_name = f"cos({num1})"
            elif choice == '9':
                result = tangent(num1)
                operation_name = f"tan({num1})"
            
            # Display result
            if result is not None:
                print(f"Result: {operation_name} = {result}\n")
        
        # EXCEPTION HANDLING: Catch any unexpected errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()