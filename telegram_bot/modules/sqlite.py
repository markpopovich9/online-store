import sqlite3
import os
db = sqlite3.connect(database= os.path.abspath(__file__ + "/../../../project/data.db"))

cursor = db.cursor()
