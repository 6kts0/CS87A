"""
Python evaluates "not" first, then "and", then "or".
"""

# Define variable
age_input = input("Enter your age\n ")
vet_stat_input = input("Are you a veteran or currently in service?\n ")

age = int(age_input)
veteran_stat = (vet_stat_input.lower() == "yes" or vet_stat_input.lower() == "y")

# if statements for age and veteran status
if (age > 60): 
    print(f"\nDiscount applied, we luv senior citizens!") 
elif (veteran_stat == True):
    print("\nDiscount applied, thank you for your service!")
elif (age < 18):
    print("\nDiscount applied, kids tickets are free!")
else:
    print("\nYou are not eligible for a discount, sorry!")