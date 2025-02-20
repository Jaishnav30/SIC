import pymysql as ps
db = "jaishnav_db"
print("------------ Database being used is -", db, "------------")
table = input("\nEnter table name: ")

def connect_db():
    return ps.Connect(  host='localhost',
                        port=3306,
                        user='root',
                        password='D@tteb@yo#106',
                        database=db,
                        charset='utf8')

def disconnect_db(connection):
    connection.close()

def create_table():
    try:
        connection = connect_db()
        query = f'''CREATE TABLE IF NOT EXISTS {table}(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    gender VARCHAR(4),
                    location VARCHAR(32),
                    dob DATETIME);'''
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        disconnect_db(connection)
        print("\nTable Created!")
    except Exception as e:
        print("\nError Creating Table:", e)

def delete_table():
    try:
        connection = connect_db()
        query = f'DROP TABLE IF EXISTS {table};'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        disconnect_db(connection)
        print("\nTable Deleted!")
    except Exception as e:
        print("\nError Deleting Table:", e)

def read_rows():
    return (
        input(f"%-25s : " % "Enter person name"),
        input(f"%-25s : " % "Enter person gender"),
        input(f"%-25s : " % "Enter person location "),
        input(f"%-25s : " % "Enter person dob (yyyy-mm-dd) ")
    )

def insert_row():
    try:
        connection = connect_db()
        query = f'INSERT INTO {table}(name, gender, location, dob) VALUES(%s, %s, %s, %s);'
        cursor = connection.cursor()
        cursor.execute(query, read_rows())
        connection.commit()
        disconnect_db(connection)
        print("\nRow Inserted!")
    except Exception as e:
        print("\nError Inserting Row:", e)

def delete_row():
    try:
        connection = connect_db()
        id = input("Enter ID to delete: ")
        query = f'DELETE FROM {table} WHERE id = {id};'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        disconnect_db(connection)
        print("\nRow Deleted!")
    except Exception as e:
        print("\nError Deleting Row:", e)

def update_row():
    try:
        connection = connect_db()
        id = input("Enter ID to update: ")
        col = input("Enter column name: ")
        val = input("Enter new value: ")

        if col.lower() in ["name", "gender", "location", "dob"]:
            val = f"'{val}'"

        query = f'UPDATE {table} SET {col} = {val} WHERE id = {id};'
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        disconnect_db(connection)
        print("\nRow Updated!")
    except Exception as e:
        print("\nError Updating Row:", e)

def display_table():
    try:
        connection = connect_db()
        query = f'SELECT * FROM {table};'
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("\nTable is Empty!")
        else:
            print("\nTable Data:")
            for row in rows:
                print(row)
        
        disconnect_db(connection)
    except Exception as e:
        print("\nError Fetching Data:", e)

create_table()

while True:
    print("\n----- MENU -----")
    print("1. Insert Row")
    print("2. Delete Row")
    print("3. Update Row")
    print("4. Display Table")
    print("5. Delete Table")
    print("6. Exit")

    choice = input("\nEnter choice: ")

    if choice == '1':
        insert_row()
    elif choice == '2':
        delete_row()
    elif choice == '3':
        update_row()
    elif choice == '4':
        display_table()
    elif choice == '5':
        delete_table()
    elif choice == '6':
        print("\nExiting Program...")
        break
    else:
        print("\nInvalid Choice! Please try again.")
