"""
Remebering python memory using sys and struct standard libraries
"""
import sys
import struct

print("\nSizing a Long float")
# Double
dub_num = 12345678901234567890.123456
print('-' * 30)
print(dub_num)
print(type(dub_num))
print('-' * 30)

# Sys size with python overhead in count (e.g. Reference count and type pointer)
print("Size when Overhead = 16")
print(f"{sys.getsizeof(dub_num)} Bytes\n" + "---------------------")
# Raw size of just the double value ()
print("Size when Overhead = 0")
print(f"{len(struct.pack('d', dub_num))} Bytes\n" + "---------------------\n")


print("Sizing a multi data type list")
# Size of mixed data type list
lst_size = [2, 329.21, (4, 1), {"Num":2}, "foo", True, 7j, [1,'fd']]
print('-' * 50)
print(f"{lst_size}")
print(type(lst_size))
print('-' * 50)

# Notice: The raw size of the list container is 64 bytes
# You can iterate through the list and process the size of each value 
print("Size when Overhead = 16 bytes")
print(f"{sys.getsizeof(lst_size)} Bytes\n" + "---------------------")