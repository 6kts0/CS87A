import csv

# Define csv file pointer
FLIGHT_DATA = 'mck_flightData.csv'

# Define to values to filter for 
TAR_CHAR = ('A', 'a')
TAR_NUM = 300
TAR_COL = 7

# Defined column names 
HEADER_LABEL = ['flight_number', 'airline_name', 'departure_city', 'departure_country', 'arrival_airport', 'arrival_city' 'arrival_country', 'passenger_count', 'flight_class', 'ticket_price']

# Flight data to write
flight_1 = ['AA101', 'American Airlines', 'New York', 'USA', 'LAX', 'Los Angeles', 'USA', 285, 'Economy', 149.99]

flight_2 = ['UA202', 'United Airlines', 'Chicago', 'USA', 'ORD', 'Chicago', 'USA', 312, 'Business', 599.99]

flight_3 = ['BA303', 'British Airways', 'London', 'UK', 'LHR', 'London', 'UK', 198, 'First', 1299.99]

flight_4 = ['DL404', 'Delta Airlines', 'Atlanta', 'USA', 'ATL', 'Atlanta', 'USA', 256, 'Economy', 179.50]

def flight_data_management():

    print('\n')
    print('-' * 66)
    print("This list is filtered by rows that start with the character 'A'  |")
    print('-' * 66)

    print('\n')
    print('+-' * 87)
    print(f'{HEADER_LABEL} |')
    print('+-' * 87)

    # Read csv filtered by a specified letter
    with open(FLIGHT_DATA, 'r') as f:
        # Using default csv reader to check the first word of each row for a pre-defined letter
        file_read = csv.reader(f, delimiter=',')

        for row in file_read:
            try:
                if row[0].startswith(TAR_CHAR):
                    print(row)
                    print('-' * 130)
            except ValueError:
                pass

    print('\n')
    print('-' * 74)
    print("This list is filtered by flights with a passenger count higher than 300  |")
    print('-' * 74)

    print('\n')
    print('+-' * 87)
    print(f'{HEADER_LABEL} |')
    print('+-' * 87)

    # Read csv filtered by a specified integer 
    with open(FLIGHT_DATA, 'r') as f:
        # Using a dictionary reader to check an individual column by name
        file_read = csv.DictReader(f, delimiter=',') 

        # Loops through the passenger_count column
        for row in file_read:
            try:
                # If a value within the passenger_count column is >= 300 the entire row containing the value is outputted
                if float(row['passenger_count']) >= TAR_NUM:
                    row_list = list(row.values()) 
                    print(row_list)
                    print('-' * 130)
            # If the list conversion goes wrong the row is skipped
            except ValueError:
                pass


    # Define data to write
    
flight_data_management()


