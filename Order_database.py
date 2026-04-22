import sqlite3

class AnalyticsDatabase:
    def __init__(self, db_name="analytics.db"): 
        self.db_name = db_name

    def connect_db(self):
        return sqlite3.connect(self.db_name)
    
    def create_table(self):
        connection = self.connect_db()
        cursor = connection.cursor()

        cursor.execute("""
CREATE TABLE IF NOT EXISTS database (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       value REAL,
                       created_at TEXT )""")
        
        connection.commit()
        connection.close()

    def Insert_Record(self):
        connection = self.connect_db()
        cursor = connection.cursor()

        record = [
            ("Sales_Q1" , "24500.75" , "2025-01-15"),
            ("Sales_Q2" , "27890.50" , "2025-04-15")
        ]

        cursor.executemany("INSERT INTO database (name,  value , created_at)VALUES (?,?,?)", record)

        connection.commit()
        connection.close()

    def Read_record(self):
        connection = self.connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM record")

        record = cursor.fetchall()

        return record
    
    def update_record(self , record_id):
        connection = self.connect_db()
        cursor = connection.cursor()

        cursor.execute("UPDATE FROM record" \
        "WHERE id  = Sales_Q2", 29500.00)

        connection.commit()
        connection.close()
    
    def Delete_record(self):
        connection = self.connect_db()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM record" \
        "WHERE id =  Sales_Q1" , name = "sales_q1")

        connection.commit()
        connection.close()

db =AnalyticsDatabase()
db.create_table()
db.Insert_Record()


