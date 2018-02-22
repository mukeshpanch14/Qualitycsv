import ReadModule as RM



def DataLength():
      a = RM.ReadModule('file.csv',1,0,',','\'')
      df = a.read_file(['Emp_Name']) 
      df['Emp_Name'] = df['Emp_Name'].astype(str)
      
      df['Length'] = df['Emp_Name'].str.len()
      print( df['Length'].max())
      #y=list(df['Length'])
      #print(max(y))
   


DataLength()
  