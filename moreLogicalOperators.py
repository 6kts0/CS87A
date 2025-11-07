"""
You can combine multiple logical operators in a single expression. Python evaluates "not" first, then "and", then "or".
"""


# Define variables
age = 62
is_student = False
is_veteran = True

# combining and, or, and not
if (age < 18 or age > 60) and is_student or is_veteran: 
    print(f"Discount applied, your veteran status is {is_veteran}.") 