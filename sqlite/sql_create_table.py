import sqlite3
create_table = """
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
text TEXT NOT NULL
);
"""

connection = sqlite3.connect("store.db")

cursor = connection.cursor()

cursor.execute(create_table)

connection.commit()

cursor.close()

connection.close()

