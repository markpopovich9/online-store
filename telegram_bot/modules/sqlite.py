import sqlite3
import os
path = os.path.abspath(__file__ + "/../../../project/data.db")
def get_data(columns = "id", table = "user"):
    db = sqlite3.connect(database=path)
    cursor = db.cursor()
    cursor.execute(f"SELECT {columns} FROM {table}")
    return cursor.fetchall()
def edit_data(name_data = "is_admin",data = 1 ,id = 1,table = "user"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    cursor.execute(f"UPDATE {table} SET {name_data} = {data} WHERE id = {id}")
    db.commit()
def counter():
    for count in range(len(get_data())):
        id = get_data()[count][0]
        edit_data(
            name_data="id",
            data= count+1,
            id=id
        )
    # db.commit()
def delete_data(id = 2, table = "user"):
    db = sqlite3.connect(database= path)
    cursor = db.cursor()
    cursor.execute(f'DELETE FROM {table} WHERE id = {id}')
    db.commit()
    counter()
    db.commit()
print(get_data(columns="id",table="product"))
