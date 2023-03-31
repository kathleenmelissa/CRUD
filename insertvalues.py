import sqlite3
conn=sqlite3.connect('company.db')
print("Connected")
conn.execute("INSERT INTO company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(1,'Andrew','Allan',21,30000.00,'Manager')");
conn.execute("INSERT INTO company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(2,'H.E.R','Ellen',30,60000.00,'Singer')");
conn.execute("INSERT INTO company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(3,'Moses','Roy',27,40000.00,'Treasurer')");
conn.execute("INSERT INTO company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(4,'Collins','Martin',28,120000.00,'P.A')");

conn.commit()
print("Successfully inserted values in company1 table")
conn.close()