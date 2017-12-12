import csv
import pandas as pd
def parse(filename):
    
    df = pd.read_csv(filename)
    #df.to_csv(filename, header=None)
    print df.to_csv(header=None,index=False)
    

def main():
    parse('EMP_MUKESH_new.csv')

if __name__ == '__main__':
    main()