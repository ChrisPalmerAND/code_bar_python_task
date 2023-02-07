import json
import csv
 
def convert_data_to_csv(all_data): 
    # Opening JSON file and loading the data
    # into the variable data
   
    # now we will open a file for writing
    data_file = open('data_file.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    
    # # Writing headers of CSV file
    header = all_data[0].keys()
    csv_writer.writerow(header)

    for person in all_data:
        # # Writing data of CSV file
        csv_writer.writerow(person.values())
    
    data_file.close()