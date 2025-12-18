"""
Faba Kouyate | Fall 2025 
"""

# Initialize main list
list_nums = [93, 65, 27, 5, 15, 69, 89, 29, 99, 73, 100, 58, 35, 72, 37, 16, 14, 48, 64, 22]

# Create three empty lists 
list_greater = []
list_odd = []
list_even = []


# Main function
def seperate_lists():
    for i in list_nums:
        if i > 10:
            list_greater.append(i)
        if i % 2 != 0:
            list_odd.append(i)
        if i % 2 == 0:
            list_even.append(i)
seperate_lists()

print('-' * 60)
print(f"Original list: {list_nums}")

# Print numbers greater than 10
# Print sum of number greater than 10
# Print list length
print('-' * 60)
print(f"All numbers greater than 10: {list_greater}")
print(f"Sum of all numbers greater than 10: {sum(list_greater)}")
print(f"List length: {len(list_greater)}")
print('-' * 60)

# Print odd numbers
# Print sum of all odd numbers
# Print list length
print(f"All odd numbers: {list_odd}")
print(f"Sum of all odd numbers: {sum(list_odd)}")
print(f"List length: {len(list_odd)}")
print('-' * 60)

# Print even numbers
# Print sum of all even numbers
# Print list length
print(f"All even numbers: {list_even}")
print(f"Sum of all even numbers: {sum(list_even)}")
print(f"List length: {len(list_even)}")
print('-' * 60)