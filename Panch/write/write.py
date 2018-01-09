import csv
file_name='write_out.csv'

with open(file_name,'a+') as file:
    sniff=csv.Sniffer()
    has_header = sniff.has_header(file.read(2048))
    print(has_reader)
    
    