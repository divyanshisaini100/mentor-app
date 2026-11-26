import sqlite3

conn = sqlite3.connect("mentor_app.db")
cursor = conn.cursor()

mentor_table = """create table mentors (
id int primary key,
name varchar(30) not null,
sst_rollno int not null unique,
)"""

cursor.execute(mentor_table)