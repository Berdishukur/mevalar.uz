import  sqlite3
conn=sqlite3.connect("sample-database (8).db")
cur=conn.cursor()
cur.execute("""
SELECT * FROM students 
INSERT INTO students (id, first_name, last_name) VALUES
(?, ?, ?),


""")
ans=cur.fetchall()
for i in ans:
    print(i)

cur.close()
conn.close()

