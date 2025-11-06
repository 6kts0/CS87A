"""
Python supports the usual logical conditions from mathematics (a == b, a < b, etc...)
"""

# Define variables
a = input("Enter an integer:  ")

# Explicitly cast input str to int
a_conv = int(a)

# Define second input variable
c = input("Enter another integer:  ")

# Explcitly Cast input str to int
c_conv = int(c)

# Define more values
b = a_conv
d = c_conv
e = b - d
f = d - b

# Print if conditional
if b > d:
    print(f"b is greater than d.\n") 
    print(f"b is greater than d by {e} by")
if d > b:
    print(f"d is greater than b.\n")
    print(f"d is greater than b by {f}.")