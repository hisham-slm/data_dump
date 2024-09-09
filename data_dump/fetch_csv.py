import csv
import os

def fetch_csv(filename: str, columns : list = None, length: int = None):
    data : list = []
    if not os.path.exists(filename):
        raise FileNotFoundError(f'{filename} not found!')
    with open(filename, 'r') as file:
        try:
            csv_reader = csv.DictReader(file)
            
            if csv_reader.fieldnames is None:
                raise ValueError('This CSV file appears to be empty or has no valid header')
            
            if columns is None:
                columns = csv_reader.fieldnames
            if not set(columns).issubset(set(csv_reader.fieldnames)):
                raise ValueError('Expected column is not in the CSV Header')
            
                
            for row in csv_reader :
                filtered_row = {key : row[key] for key in columns}
                data.append(filtered_row)

            if length is None or length > len(data):
                length = len(data)
            data = [tuple(row[key] for key in columns) for row in data]

            return data[:length]
            
            
        except csv.Error as error:
            return error 