import locale
try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    print("Could not set time to UTF-8 - Defaulting(en_US)")
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except locale.Error:
        print("Couldnt connect to locale")

# Define base class and define values as objects within the class
class Ford:
    def __init__(self, Model, MSRP):
        self.Model = Model
        self.MSRP = MSRP

# Fetch inputs for model and msrp once for Ford make
frd_model = input("Enter any Ford model: ")
frd_MSRP_in = input("Enter the base MSRP: ")
frd_intMSRP = int(frd_MSRP_in) 
frd_MSRP = locale.currency(frd_intMSRP, grouping=True) # Convert MSRP input to USD currency

frd = Ford(frd_model, frd_MSRP)

class BMW:
    def __init__(self, Model, MSRP):
        self.Model = Model
        self.MSRP = MSRP

# Fetch inputs for model and msrp once for BMW make
bmw_model = input("Enter any BMW model: ")
bmw_MSRP_in = input("Enter the base MSRP: ")
bmw_intMSRP = int(bmw_MSRP_in)
bmw_MSRP = locale.currency(bmw_intMSRP, grouping=True) # Convert MSRP input to USD currency

bmw = BMW(bmw_model, bmw_MSRP)

print("==================")
print(frd.Model)
print(frd.MSRP)
print("==================")
print(bmw.Model)
print(bmw.MSRP)
print("==================")
