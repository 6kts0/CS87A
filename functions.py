"""
def(definition): Used to define a function
    * Signals the start of a function
"""
# -+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+- #
"""
return: Used to exit a function and pass a variable
    * Allows a function to produce an output
    * If return is not used "None" will be passed by default
"""
---------------------------------
# Define function 1 
# Set dictionairy values to return
def car_1(): 
    return {
    "Model": "MustangGTD",
    "Manufacturer": "Ford",
    "Type": "Track",
    "MSRP": "$327,100",
    "Horsepower": "875 hp"
} 
# Define function 2
# Set dictionairy values to return
def car_2():
    return {
    "Model": "Corvette Z07",
    "Make": "Chevrolet",
    "Type": "Sport",
    "MSRP": "$112,100",
    "Horsepower": "923 hp"  
    }

# Set dictionairy to seperate variable
car_1 = car_1()
car_2 = car_2()

print(f"Car_1 specs: {car_1}")
print(f"\nCar_2 specs: {car_2}")

# -+-+-+-+-+-+-+ +-+-+-+-+-+-+-+ +-+-+-+-+-+-+- #

def check_temp(temp): 
    if temp >= 100:
        return "Boiling!"
    elif temp <= 30:  
        return "Freezing!"
    elif temp >= 69:
        return "Temp is getting hot"
    else: 
        return "Temp is normal"

print(f"\nTemp Status: {check_temp(66)}")