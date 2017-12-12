from datetime import datetime

fields = ("Emp_Id", "Emp_Name", "City", "DOB")

class FundingRecord(namedtuple('FundingRecord_', fields)):

    @classmethod
    def parse(klass, row):
        row = list(row)                                # Make row mutable
        row[1] = int(row[1]) if row[1] else None       # Convert "numEmps" to an integer
        row[4] = datetime.strptime(row[4], "%d-%b-%y") # Parse the "fundedDate"
      #  row[7] = int(row[7])                           # Convert "raisedAmt" to an integer
        return klass(*row)

    def __str__(self):
        date = self.fundedDate.strftime("%d %b, %Y")
        return "%s raised %i in round %s on %s" % (self.Emp_Name, self.Emp_Id, self.City, date)

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