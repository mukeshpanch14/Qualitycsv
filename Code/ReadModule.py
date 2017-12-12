import pandas

class ReadModule():
    
    def __init__(self,filename,header_count,footer_count,delimiter):
        self.filename = filename
        self.header_count =