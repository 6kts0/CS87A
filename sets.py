"""
A set is a mutuable unordered collection of elements
    * Can store different data types.
    * Does not maintain order of elements.
    * Elements can be added or removed.
"""

# Define two sets and define variables to hold sums
account_1 = {200, 211, 192, 73}
account_2 = {122, 49, 102, 265}
acc1_sum = sum(account_1)
acc2_sum = sum(account_2)

# Calculating sum of numbers in account_2 set
if acc1_sum > 500:
    print("\nThe total of account 1 is more than $500")
    print(f"Amount held in account 1: ${acc1_sum}")
else:
    print("Account 1 is below $500")

# Calculating sum of numbers in account_2 set
if acc2_sum > 500:
    print("\nThe total of account 2 is more than $500")
    print(f"Amount held in account 2: ${acc2_sum}") 
else: 
    print("Account 2 is below $500")