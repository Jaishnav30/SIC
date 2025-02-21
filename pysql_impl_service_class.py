import pysql_jai as ps

class Table_service:
    def __init__(self):
        self.oprs = ps.DBMS()
        
    def create_table(self):
        self.oprs.create_table()
        
    def insert_row(self):
        self.oprs.insert_row()
    
    def delete_row(self):
        self.oprs.delete_row()
        
    def update_row(self):
        self.oprs.update_row()
    
    def display_table(self):
        self.oprs.display_table()
    
    def delete_table(self):
        self.oprs.delete_table()
    
    def search(self):
        self.oprs.search()