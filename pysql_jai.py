import pymysql as ps

db = "jaishnav_db"
print("------------ Database being used is -", db, "------------")

class DBMS:
    def __init__(self):
        self.db = db
        self.table = input("\nEnter table name: ")

    def connect_db(self):
        return ps.connect(
            host='localhost',
            port=3306,
            user='root',
            password='D@tteb@yo#106',
            database=self.db,
            charset='utf8'
        )

    def disconnect_db(self, connection):
        connection.close()

    def create_table(self):
        try:
            connection = self.connect_db()
            query = f'''CREATE TABLE IF NOT EXISTS {self.table}(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(50) NOT NULL,
                        gender VARCHAR(4),
                        location VARCHAR(32),
                        dob DATETIME);'''
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.disconnect_db(connection)
            print("\nTable Created!")
        except Exception as e:
            print("\nError Creating Table:", e)

    def delete_table(self):
        try:
            connection = self.connect_db()
            query = f'DROP TABLE IF EXISTS {self.table};'
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.disconnect_db(connection)
            print("\nTable Deleted!")
        except Exception as e:
            print("\nError Deleting Table:", e)

    def read_rows(self):
        return (
            input(f"%-35s : " % "Enter person name"),
            input(f"%-35s : " % "Enter person gender"),
            input(f"%-35s : " % "Enter person location"),
            input(f"%-35s : " % "Enter person dob (yyyy-mm-dd)")
        )

    def insert_row(self):
        try:
            connection = self.connect_db()
            query = f'INSERT INTO {self.table}(name, gender, location, dob) VALUES(%s, %s, %s, %s);'
            cursor = connection.cursor()
            cursor.execute(query, self.read_rows())
            connection.commit()
            self.disconnect_db(connection)
            print("\nRow Inserted!")
        except Exception as e:
            print("\nError Inserting Row:", e)

    def delete_row(self):
        try:
            connection = self.connect_db()
            row_id = input("Enter ID to delete: ")
            query = f'DELETE FROM {self.table} WHERE id = {row_id};'
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.disconnect_db(connection)
            print("\nRow Deleted!")
        except Exception as e:
            print("\nError Deleting Row:", e)

    def update_row(self):
        try:
            connection = self.connect_db()
            row_id = input("Enter ID to update: ")
            col = input("Enter column name: ")
            val = input("Enter new value: ")

            if col.lower() in ["name", "gender", "location", "dob"]:
                val = f"'{val}'"

            query = f'UPDATE {self.table} SET {col} = {val} WHERE id = {row_id};'
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            self.disconnect_db(connection)
            print("\nRow Updated!")
        except Exception as e:
            print("\nError Updating Row:", e)

    def display_table(self):
        try:
            connection = self.connect_db()
            query = f'SELECT * FROM {self.table};'
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            if not rows:
                print("\nTable is Empty!")
            else:
                print("\nTable Data:")
                for row in rows:
                    print(row)

            self.disconnect_db(connection)
        except Exception as e:
            print("\nError Fetching Data:", e)

    def search(self):
        try:
            connection = self.connect_db()
            row_id = input("Enter ID to search: ")
            query = f'SELECT * FROM {self.table} WHERE id = {row_id};'
            cursor = connection.cursor()
            cursor.execute(query)
            row = cursor.fetchone()

            if not row:
                print("\nData not found!")
            else:
                print("\nRow Data:")
                for r in row:
                    print(r)
            self.disconnect_db(connection)
        except Exception as e:
            print("\nError Searching Row:", e)



# create_table()

# while True:
#     print("\n----- MENU -----")
#     print("1. Insert Row")
#     print("2. Delete Row")
#     print("3. Update Row")
#     print("4. Display Table")
#     print("5. Delete Table")
#     print("6. Search")
#     print("7. Exit")

#     choice = input("\nEnter choice: ")

#     if choice == '1':
#         insert_row()
#     elif choice == '2':
#         delete_row()
#     elif choice == '3':
#         update_row()
#     elif choice == '4':
#         display_table()
#     elif choice == '5':
#         delete_table()
#     elif choice == '6':
#         search()
#     elif choice == '7':
#         print("\nExiting Program...")
#         break
#     else:
#         print("\nInvalid Choice! Please try again.")
