import ReadModule as RM



def DataLength():
      a = RM.ReadModule('file.csv',1,0,',','\'')
      df = a.read_file(['DOB']) 
      df['DOB'] = df['DOB'].astype(str)
      
      df['Length'] = df['DOB'].str.len()
      print( df['Length'])
      y=list(df['Length'])
      print(max(y))
   


DataLength()
  