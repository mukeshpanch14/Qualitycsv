import csv
import pandas as pd

def read_funding_data(path):
    with open(path, 'rU') as data:
        data.readline()            # Skip the header
        reader = csv.reader(data)  # Create a regular tuple reader
        for row in map(FundingRecord.parse, reader):
            yield row

if __name__ == "__main__":
    for row in read_funding_data(EMP_MUKESH_new.csv):
        print row
        break