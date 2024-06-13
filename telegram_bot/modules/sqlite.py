import sqlite3
import os
def get_data(columns, table = "user"):
    db = sqlite3.connect(database= os.path.abspath(__file__ + "/../../../project/data.db"))
    cursor = db.cursor()
    cursor.execute(f"SELECT {columns} FROM {table}")
    return cursor.fetchall()
def edit_data(name_data = "is_admin",data = 1 ,id = 1,table = "user"):
    db = sqlite3.connect(database= os.path.abspath(__file__ + "/../../../project/data.db"))
    cursor = db.cursor()
    cursor.execute(f"UPDATE {table} SET {name_data} = {data} WHERE id = {id}")
    db.commit()
print(get_data(columns="id",table="product"))
