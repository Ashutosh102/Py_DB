import sqlite3
conn=sqlite3.connect("employee.db")
cur=conn.cursor()
if cur:
    print("Database is created")
else:
    print("Not connected DB")
sql='''CREATE TABLE emp_2(EID Integer PRIMARY KEY AUTOINCREMENT,
                                                   ENAME varchar(30) NOT NULL,
                                                   DoB date,
                                                   DoJ date,
                                                   Salary real);'''
if cur.execute(sql):
    print("Table Is created succesfully")
else:
    print("Not created table")
conn.commit()
sqlite_insert_query = """INSERT INTO emp_2
                          (EID, ENAME, DoB, Salary) 
                           VALUES 
                          (1,'James','2002-11-15',8000)"""

count = cur.execute(sqlite_insert_query)
conn.commit()
print("Record inserted successfully into developers table ", cur.rowcount)
sqlite_select_query = """SELECT * from emp_2"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("BirthDate: ", row[2])
            print("Salary: ", row[3])
            print("\n")

'''
WAP a python code to create a student DB in sqliteDB> And perform folowing operations:
1/ Create a table (stu_table)
2/ Insert 10 records into that
3/ List the student details....who have secured marks<12 in each subject
4/ Update the student marks in the subject, where they secured<12.......add 5 marks to each
'''




