import csv

# Define csv file constant
FLIGHT_DATA = 'mck_flightData.csv'

# Define to contant filter values 
TAR_CHAR = 'A'
TAR_NUM = 300
TAR_COL = 7

# Define range for last four rows + the appended rows
ROW_CHECK = [36, 38, 39, 40, 41, 42, 43, 44] 

# Define column header names to display
HEADER_LABEL = ['flight_number' ' | ' 'airline_name' ' | ' 'departure_city' ' | ' 'departure_country' ' | ' 'arrival_airport' ' | ' 'arrival_city' ' | ' 'arrival_country' ' | ' 'passenger_count' ' | ' 'flight_class' ' | ' 'ticket_price']

# Flight data to write
flight_1 = ['AA101', 'American Airlines', 'New York', 'USA', 'LAX', 'Los Angeles', 'USA', '285', 'Economy', '149.99']

flight_2 = ['UA202', 'United Airlines', 'Chicago', 'USA', 'ORD', 'Chicago', 'USA', '312', 'Business', '599.99']

flight_3 = ['BA303', 'British Airways', 'London', 'UK', 'LHR', 'London', 'UK', '198', 'First', '1299.99']

flight_4 = ['DL404', 'Delta Airlines', 'Atlanta', 'USA', 'ATL', 'Atlanta', 'USA', '256', 'Economy', '179.50']

# Function starts
def flight_data_management():

    print('\n')
    print('-' * 67)
    print("| This list is filtered by rows that start with the character 'A' |")
    print('-' * 67)

    print('\n')
    print('+-' * 84)
    print(HEADER_LABEL)
    print('+-' * 84)

    # Read csv filtered by a specified letter
    with open(FLIGHT_DATA, 'r') as f:
        file_read = csv.reader(f, delimiter=',') # Using default csv reader to check the first word of each row for a pre-defined letter
        next(file_read)

        for row in file_read:
            try:
                if len(row) > 0 and row[0].startswith(TAR_CHAR):
                    print(row)
                    print('-' * 130)
            except ValueError:
                pass

    print('\n')
    print('-' * 74)
    print("| This list is filtered to flights with a passenger count of 300 or higher |")
    print('-' * 74)

    print('\n')
    print('+-' * 84)
    print(f'{HEADER_LABEL} |')
    print('+-' * 84)

    # Read csv filtered by a specified integer 
    with open(FLIGHT_DATA, 'r+') as f:
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

    # Writing data from flights 1, 2, 3, and 4
    # 'a' = append to csv
    # Using just 'w' or 'w+' will overwrite all existing data in the csv
    with open(FLIGHT_DATA, 'a') as f:
        file_write = csv.writer(f, delimiter=',', lineterminator='\n')
        file_write.writerow(flight_1) # Adding flight 1
        file_write.writerow(flight_2) # Adding flight 2
        file_write.writerow(flight_3) # Adding flight 3 
        file_write.writerow(flight_4) # Adding flight 4  

    print('\n')
    print('-' * 100)
    print("| This list contains data appended within the last 48 hours, along with the previous 4 rows of data |")
    print('-' * 100)

    print('\n')
    print('+-' * 84)
    print(HEADER_LABEL)
    print('+-' * 84)


    # Open csv and output the new rows along with the previous last 4 rows of data
    with open(FLIGHT_DATA, 'r') as f:
        file_read = csv.reader(f, delimiter=',', )
        for i, row in enumerate(file_read):
            if i in ROW_CHECK:
                print(','.join(row))
                print('-' * 130)

def main():
    return flight_data_management()

if __name__ == "__main__":
    main()
