import sqlite3
conn=sqlite3.connect('company.db')
print("Successfully opened database")

conn.execute("""CREATE TABLE Company1(
ID INT PRIMARY KEY  NOT NULL ,
FIRSTNAME TEXT NOT NULL ,
LASTNAME TEXT NOT NULL ,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(20))""")

print("Successfully created company1 table")
conn.close()