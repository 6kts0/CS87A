"""
Python is a dynamically typed, object oriented programming language.
A variable is a pointer to a location in memory.
"""
numerator = 100
denominator = float(input("Enter a positive number: "))
result = 0

try:
    # Using "try" to run the erroneous code
    print("Trying the division...")
    result = numerator / denominator
    print("This line will not be reached.")

except ZeroDivisionError:
    # This block only runs if a ZeroDivisionError happens
    print("Error! You tried to divide by zero.")
    print("Setting result to 'None' (or 0, or some safe value).")
    result = None

# The program continues instead of crashing
print("-" * 60)
print(f"The final result is: {result}")

