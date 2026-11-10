#sql = structured query language
import sqlite3

con = sqlite3.connect("bank.db")

cur = con.cursor()
# this means that we are creating a table


cur.execute('''  CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(10) UNIQUE NOT NULL,
            email VARCHAR(10) UNIQUE NOT NULL,
            pin INTEGER NOT NULL,
            amount REAL DEFAULT 0.00
            )
            ''')


con.commit()
con.close()